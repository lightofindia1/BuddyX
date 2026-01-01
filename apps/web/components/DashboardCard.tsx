import React, { ReactNode } from "react";

interface DashboardCardProps {
  title: string;
  children: ReactNode;
  action?: {
    label: string;
    onClick: () => void;
    variant?: "button" | "link";
  };
  gradient?: string;
  icon?: string;
}

const DashboardCard: React.FC<DashboardCardProps> = ({ 
  title, 
  children, 
  action, 
  gradient = "from-[#667eea] to-[#764ba2]",
  icon 
}) => {
  return (
    <div className="group relative bg-white/90 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-white/60 backdrop-blur-md">
      {/* Card content */}
      <div className="relative p-6">
        {/* Header with icon */}
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center space-x-3">
            {icon && (
              <div className={`w-10 h-10 rounded-xl bg-gradient-to-br ${gradient} flex items-center justify-center text-white text-lg shadow-lg`}>
                {icon}
              </div>
            )}
            <h3 className="text-xl font-bold text-gray-800">{title}</h3>
          </div>
        </div>
        {/* Content */}
        <div className="mb-6">
          {children}
        </div>
        {/* Action button */}
        {action && (
          <div className="flex justify-end">
            {action.variant === "link" ? (
              <button
                onClick={action.onClick}
                className="text-[#667eea] hover:text-[#764ba2] text-sm font-semibold transition-colors duration-200 hover:underline"
              >
                {action.label} →
              </button>
            ) : (
              <button
                onClick={action.onClick}
                className={`bg-gradient-to-r ${gradient} text-white px-6 py-2 rounded-xl hover:shadow-lg transform hover:-translate-y-0.5 transition-all duration-200 text-sm font-semibold`}
              >
                {action.label}
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default DashboardCard; 