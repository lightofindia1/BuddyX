import React, { useEffect } from "react";
import { useAuth } from "../components/AuthContext";
import { useRouter } from "next/router";
import Navbar from "../components/Navbar";

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
    <>
      <Navbar />
      <main className="flex flex-col items-center justify-center min-h-screen">
        <h1 className="text-4xl font-bold mb-4">Welcome to BuddyX</h1>
        <p className="text-lg">Your secure, cross-platform personal assistant.</p>
        <p className="mt-4">Logged in as <span className="font-mono">{user.username}</span></p>
      </main>
    </>
  );
};

export default HomePage; 