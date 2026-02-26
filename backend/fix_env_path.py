#!/usr/bin/env python3
"""
Fix the CHUNKS_PATH in .env file to be relative to current directory
"""

import os

def fix_env_path():
    env_file = '.env'
    
    # Read current .env file
    lines = []
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    # Update CHUNKS_PATH line
    updated_lines = []
    for line in lines:
        if line.startswith('CHUNKS_PATH='):
            updated_lines.append('CHUNKS_PATH=./chunks.json\n')
        else:
            updated_lines.append(line)
    
    # Write back
    with open(env_file, 'w') as f:
        f.writelines(updated_lines)
    
    print("✅ Updated CHUNKS_PATH to ./chunks.json in .env file")

if __name__ == "__main__":
    fix_env_path()
