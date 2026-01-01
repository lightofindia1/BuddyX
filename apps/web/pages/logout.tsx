import { useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from "../components/AuthContext";

export default function LogoutPage() {
    const router = useRouter();
    const { logout } = useAuth();

    useEffect(() => {
        const handleLogout = async () => {
            await logout();
            router.push('/login');
        };

        handleLogout();
    }, [router]);

    return (
        <div className="flex items-center justify-center min-h-screen">
            <p className="text-lg">Logging out...</p>
        </div>
    );
}