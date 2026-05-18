from pathlib import Path
import json

def omit_suppressed(sarif: dict) -> dict:
    for run in sarif['runs']:
        run['results'] = [i for i in run['results'] if 'suppressions' not in i]
    return sarif

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Expected argument: input SARIF file", file=sys.stderr)
        sys.exit(1)

    sarif_path = Path(sys.argv[1])
    if not sarif_path.exists():
        print(f"'{sarif_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    with open(sarif_path, 'r') as f:
        sarif = json.load(f)

    filtered_sarif = omit_suppressed(sarif)

    if len(sys.argv) >= 3: 
        output = Path(sys.argv[2])
        with open(output, 'w') as f:
            f.write(f"{json.dumps(filtered_sarif)}")

    else:
        print(f"{json.dumps(filtered_sarif)}")
    
