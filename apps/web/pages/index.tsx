import React, { useEffect } from "react";
import { useAuth } from "../components/AuthContext";
import { useRouter } from "next/router";
// import Sidebar from "../components/Sidebar";
import Dashboard from "../components/Dashboard";

const HomePage = () => {
  const { user, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !user) {
      router.replace("/login");
    }
  }, [user, loading, router]);

  if (loading) {
    return (
      <main className="flex flex-col items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
        <p>Loading...</p>
      </main>
    );
  }

  if (!user) return null;

  return (
    <div className="flex h-screen bg-gray-50">
      {/* <Sidebar activeItem="home" /> */}
      <Dashboard />
    </div>
  );
};

export default HomePage; 