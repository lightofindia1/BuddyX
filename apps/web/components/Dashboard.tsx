import React from "react";
import DashboardCard from "./DashboardCard";

const DASHBOARD_GRADIENT = "from-[#667eea] to-[#764ba2]";

const Dashboard: React.FC = () => {
  const handleViewAll = () => {};
  const handleUpload = () => {};
  const handleNewItem = () => {};
  const handleAddEntry = () => {};
  const handleNewEntry = () => {};
  const handleAddMemory = () => {};

  return (
    <div className="flex-1 min-h-screen bg-gradient-to-br from-[#667eea] to-[#764ba2]">
      {/* Header */}
      <div className="relative p-8">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-4xl font-bold bg-gradient-to-r from-[#667eea] to-[#764ba2] bg-clip-text text-transparent">Welcome back! 👋</h1>
            <p className="text-gray-700 mt-2">Here's what's happening today</p>
          </div>
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <span className="text-gray-400">🔍</span>
            </div>
            <input
              type="text"
              placeholder="Search anything..."
              className="w-80 pl-12 pr-4 py-3 bg-white/80 backdrop-blur-sm border border-gray-200 rounded-2xl focus:outline-none focus:ring-2 focus:ring-[#667eea] focus:border-transparent shadow-lg"
            />
          </div>
        </div>
      </div>
      {/* Dashboard Grid */}
      <div className="px-8 pb-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <DashboardCard title="Emails" icon="📧" gradient={DASHBOARD_GRADIENT} action={{ label: "View all", onClick: handleViewAll, variant: "link" }}>
            {/* ...card content unchanged... */}
            <div className="space-y-4">
              <div className="flex justify-between items-start p-3 bg-white/80 rounded-xl shadow-sm">
                <div>
                  <p className="font-semibold text-gray-800">Amanda Tomorrow</p>
                  <p className="text-sm text-gray-600">Amanda Clark</p>
                </div>
                <span className="text-xs bg-[#667eea]/10 text-[#667eea] px-2 py-1 rounded-full font-medium">Jul 11</span>
              </div>
              <div className="flex justify-between items-start p-3 bg-white/80 rounded-xl shadow-sm">
                <div>
                  <p className="font-semibold text-gray-800">Project Update</p>
                  <p className="text-sm text-gray-600">James Smith</p>
                </div>
                <span className="text-xs bg-[#764ba2]/10 text-[#764ba2] px-2 py-1 rounded-full font-medium">Jul 9</span>
              </div>
              <div className="flex justify-between items-start p-3 bg-white/80 rounded-xl shadow-sm">
                <div>
                  <p className="font-semibold text-gray-800">Weekend Plan</p>
                  <p className="text-sm text-gray-600">Lisa White</p>
                </div>
                <span className="text-xs bg-[#667eea]/10 text-[#667eea] px-2 py-1 rounded-full font-medium">Jul 8</span>
              </div>
            </div>
          </DashboardCard>
          <DashboardCard title="Files" icon="📁" gradient={DASHBOARD_GRADIENT} action={{ label: "Upload", onClick: handleUpload }}>
            <div className="space-y-4">
              <div className="flex items-center space-x-4 p-3 bg-white/80 rounded-xl shadow-sm">
                <span className="text-2xl">📄</span>
                <div className="flex-1">
                  <p className="font-semibold text-gray-800">Document.pdf</p>
                  <p className="text-xs text-gray-500">2.3 MB • Updated 2h ago</p>
                </div>
              </div>
              <div className="flex items-center space-x-4 p-3 bg-white/80 rounded-xl shadow-sm">
                <span className="text-2xl">📊</span>
                <div className="flex-1">
                  <p className="font-semibold text-gray-800">Presentation.pptx</p>
                  <p className="text-xs text-gray-500">15.7 MB • Updated 1d ago</p>
                </div>
              </div>
              <div className="flex items-center space-x-4 p-3 bg-white/80 rounded-xl shadow-sm">
                <span className="text-2xl">🖼️</span>
                <div className="flex-1">
                  <p className="font-semibold text-gray-800">Photo.jpg</p>
                  <p className="text-xs text-gray-500">3.1 MB • Updated 3d ago</p>
                </div>
              </div>
            </div>
          </DashboardCard>
          <DashboardCard title="Vault" icon="🔒" gradient={DASHBOARD_GRADIENT} action={{ label: "New Item", onClick: handleNewItem }}>
            <div className="space-y-4">
              <div className="flex items-center justify-between p-3 bg-white/80 rounded-xl shadow-sm cursor-pointer">
                <div className="flex items-center space-x-3">
                  <span className="text-xl">🔒</span>
                  <span className="font-semibold text-gray-800">Gmail</span>
                </div>
                <span className="text-[#764ba2] font-bold">→</span>
              </div>
              <div className="flex items-center justify-between p-3 bg-white/80 rounded-xl shadow-sm cursor-pointer">
                <div className="flex items-center space-x-3">
                  <span className="text-xl">⭕</span>
                  <span className="font-semibold text-gray-800">note 1</span>
                </div>
                <span className="text-[#667eea] font-bold">→</span>
              </div>
            </div>
          </DashboardCard>
          <DashboardCard title="Calendar" icon="📅" gradient={DASHBOARD_GRADIENT} action={{ label: "Add entry", onClick: handleAddEntry }}>
            <div className="space-y-4">
              <div className="text-center p-3 bg-white/80 rounded-xl shadow-sm">
                <p className="font-bold text-gray-800 text-lg">July 2025</p>
              </div>
              <div className="space-y-3">
                <div className="flex items-center space-x-3 p-2 bg-white/80 rounded-lg">
                  <span className="text-sm font-bold text-[#667eea] bg-[#667eea]/10 px-2 py-1 rounded-full">12</span>
                  <span className="text-gray-800 font-medium">John's Birthday</span>
                </div>
                <div className="flex items-center space-x-3 p-2 bg-white/80 rounded-lg ml-4">
                  <span className="text-gray-800">• Submit report</span>
                </div>
                <div className="flex items-center space-x-3 p-2 bg-white/80 rounded-lg">
                  <input type="checkbox" className="rounded border-gray-300 text-[#667eea] focus:ring-[#667eea]" />
                  <span className="text-gray-800">Buy groceries</span>
                </div>
              </div>
            </div>
          </DashboardCard>
          <DashboardCard title="Journal" icon="📓" gradient={DASHBOARD_GRADIENT} action={{ label: "New entry", onClick: handleNewEntry }}>
            <div className="space-y-4">
              <div className="text-center p-3 bg-white/80 rounded-xl shadow-sm">
                <p className="font-bold text-gray-800">July 12, 2025</p>
              </div>
              <div className="space-y-3">
                <div className="text-center p-3 bg-white/80 rounded-xl">
                  <p className="text-2xl mb-2">😊</p>
                  <p className="font-semibold text-gray-800">Mood!</p>
                </div>
                <div className="p-3 bg-white/80 rounded-xl">
                  <p className="text-gray-600 text-sm italic">"It was a productive day..."</p>
                </div>
              </div>
            </div>
          </DashboardCard>
          <DashboardCard title="MemoryMap" icon="🧭" gradient={DASHBOARD_GRADIENT} action={{ label: "Add memory", onClick: handleAddMemory }}>
            <div className="space-y-3">
              <div className="text-center p-3 bg-white/80 rounded-xl shadow-sm">
                <p className="font-bold text-gray-800 text-lg">1995</p>
              </div>
              <div className="space-y-2">
                <div className="flex items-center space-x-2 p-2 bg-white/80 rounded-lg">
                  <span className="w-2 h-2 bg-[#667eea] rounded-full"></span>
                  <span className="text-gray-700">First School</span>
                </div>
                <div className="flex items-center space-x-2 p-2 bg-white/80 rounded-lg">
                  <span className="w-2 h-2 bg-[#764ba2] rounded-full"></span>
                  <span className="text-gray-700">Won Science Fair</span>
                </div>
                <div className="flex items-center space-x-2 p-2 bg-white/80 rounded-lg">
                  <span className="w-2 h-2 bg-[#667eea] rounded-full"></span>
                  <span className="text-gray-700">Graduated</span>
                </div>
                <div className="flex items-center space-x-2 p-2 bg-white/80 rounded-lg">
                  <span className="w-2 h-2 bg-[#764ba2] rounded-full"></span>
                  <span className="text-gray-700">Built BuddyX</span>
                </div>
              </div>
            </div>
          </DashboardCard>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 