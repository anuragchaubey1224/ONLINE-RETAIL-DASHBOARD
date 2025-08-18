#!/usr/bin/env python3
"""
Simple script to run the Online Retail Dashboard
"""
import subprocess
import sys
import os

def main():
    print("🚀 Starting Online Retail Dashboard...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('dashboard.py'):
        print("❌ Error: dashboard.py not found in current directory")
        print("Please run this script from the project root directory")
        return
    
    # Check if featured data exists
    if not os.path.exists('data/featured_data.csv'):
        print("❌ Error: Featured data not found!")
        print("🔧 Running feature engineering first...")
        try:
            subprocess.run([sys.executable, 'src/feature_engineering.py'], check=True)
            print("✅ Feature engineering completed!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running feature engineering: {e}")
            return
    
    # Start the dashboard
    print("🌟 Starting Streamlit Dashboard...")
    print("📊 Dashboard will be available at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the dashboard")
    print("=" * 50)
    
    try:
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'dashboard.py'])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Thank you!")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    main()
