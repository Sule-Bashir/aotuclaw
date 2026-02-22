cat > scripts/check_moltbook_logs.py << 'EOF'
#!/usr/bin/env python3
"""Check Moltbook logs for hackathon verification"""

import os
from pathlib import Path

log_path = Path.home() / '.openclaw' / 'logs' / 'moltbook.log'

print("=" * 50)
print("📱 AutoClaw Moltbook Log Checker")
print("=" * 50)

if log_path.exists():
    print(f"\n✅ Log file found: {log_path}")
    print("\n📋 Last 10 posts:")
    print("-" * 40)
    
    with open(log_path, 'r') as f:
        lines = f.readlines()
        for line in lines[-10:]:
            print(line.strip())
else:
    print(f"\n❌ Log file not found at {log_path}")
    print("Run main.py first to generate logs")

print("\n✅ Copy this to Discord as proof of Moltbook activity")
EOF

chmod +x scripts/check_moltbook_logs.py
