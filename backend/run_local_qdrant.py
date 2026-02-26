#!/usr/bin/env python3
"""
Start a local Qdrant instance for testing
"""

import subprocess
import time
import requests
from qdrant_client import QdrantClient

def start_local_qdrant():
    """Start local Qdrant using Docker"""
    print("Starting local Qdrant...")
    
    # Check if Docker is running
    try:
        subprocess.run(["docker", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Docker not found. Please install Docker first.")
        return False
    
    # Start Qdrant container
    cmd = [
        "docker", "run", "-d", "--name", "qdrant-test",
        "-p", "6333:6333", "-p", "6334:6334",
        "qdrant/qdrant:latest"
    ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True)
        container_id = result.stdout.decode().strip()
        print(f"✅ Qdrant container started: {container_id}")
        
        # Wait for Qdrant to be ready
        print("Waiting for Qdrant to be ready...")
        for i in range(30):
            try:
                response = requests.get("http://localhost:6333/health", timeout=5)
                if response.status_code == 200:
                    print("✅ Qdrant is ready!")
                    print("\nUpdate your .env file with:")
                    print("QDRANT_URL=http://localhost:6333")
                    print("QDRANT_API_KEY=")
                    return True
            except:
                pass
            time.sleep(1)
        
        print("❌ Qdrant failed to start within 30 seconds")
        return False
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start Qdrant: {e}")
        return False

def stop_local_qdrant():
    """Stop local Qdrant container"""
    try:
        subprocess.run(["docker", "stop", "qdrant-test"], check=True, capture_output=True)
        subprocess.run(["docker", "rm", "qdrant-test"], check=True, capture_output=True)
        print("✅ Local Qdrant stopped")
    except subprocess.CalledProcessError:
        pass

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "stop":
        stop_local_qdrant()
    else:
        start_local_qdrant()
