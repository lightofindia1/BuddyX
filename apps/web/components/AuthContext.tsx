import React, { createContext, useContext, useEffect, useState, useCallback } from "react";
import api from "@/../../packages/api-client";
import { jwtDecode } from "jwt-decode";
import { useRouter } from "next/router";

interface User {
  username: string;
  [key: string]: any;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  token: string | null;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const router = useRouter();

  // Helper to refresh token
  const refreshToken = useCallback(async () => {
    try {
      const response = await api.post("/auth/refresh", {}, {
        headers: { Authorization: `Bearer ${token}` },
      });
      const { access_token } = response.data;
      localStorage.setItem("token", access_token);
      setToken(access_token);
      const decoded: any = jwtDecode(access_token);
      setUser({ username: decoded.sub, ...decoded });
      return access_token;
    } catch {
      logout();
      return null;
    }
  }, [token]);

  useEffect(() => {
    let timeout: NodeJS.Timeout | null = null;
    const storedToken = localStorage.getItem("token");
    if (storedToken) {
      setToken(storedToken);
      try {
        const decoded: any = jwtDecode(storedToken);
        setUser({ username: decoded.sub, ...decoded });
        // Set up token refresh before expiry
        if (decoded.exp) {
          const expiresIn = decoded.exp * 1000 - Date.now();
          if (expiresIn > 0) {
            timeout = setTimeout(() => {
              refreshToken();
            }, Math.max(expiresIn - 60000, 1000)); // refresh 1 min before expiry
          }
        }
      } catch {
        setUser(null);
        setToken(null);
        localStorage.removeItem("token");
      }
    }
    setLoading(false);
    return () => {
      if (timeout) clearTimeout(timeout);
    };
  }, [refreshToken]);

  const login = async (username: string, password: string) => {
    setLoading(true);
    try {
      const response = await api.post("/auth/login", { username, password });
      const { access_token } = response.data;
      localStorage.setItem("token", access_token);
      setToken(access_token);
      const decoded: any = jwtDecode(access_token);
      setUser({ username: decoded.sub, ...decoded });
      setLoading(false);
      router.push("/");
    } catch (err) {
      setLoading(false);
      throw err;
    }
  };

  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem("token");
    router.push("/login");
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout, token }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}; 