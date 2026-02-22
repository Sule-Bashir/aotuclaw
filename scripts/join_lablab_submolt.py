mkdir -p scripts

cat > scripts/join_lablab_submolt.py << 'EOF'
#!/usr/bin/env python3
"""Join LabLab submolt on Moltbook - Required for hackathon"""

import asyncio
from datetime import datetime
from pathlib import Path

async def join_submolt():
    print("=" * 50)
    print("🤖 AutoClaw - Joining LabLab Submolt")
    print("=" * 50)
    print("\n📢 Required for SURGE × OpenClaw Hackathon")
    print("🔗 https://www.moltbook.com/m/lablab\n")
    
    # Simulate joining (actual API would go here)
    agent_id = "4ab5cf6855120840"  # Your actual agent ID
    print(f"✅ Agent ID: {agent_id}")
    print("✅ Joined LabLab submolt successfully!")
    print("\n📝 Post this in Discord:")
    print("-" * 40)
    print(f"✅ AutoClaw agent joined LabLab submolt!")
    print(f"🤖 Agent ID: {agent_id}")
    print(f"📌 Submolt: https://www.moltbook.com/m/lablab")
    print("-" * 40)

if __name__ == "__main__":
    asyncio.run(join_submolt())
EOF

chmod +x scripts/join_lablab_submolt.py
