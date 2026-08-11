import subprocess
import sys

def run_command(cmd):
    print(f"\n> {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print("Command failed.")
        sys.exit(1)

def show_status():
    print("\n" + "=" * 50)
    print(" Kubernetes Status")
    print("=" * 50)

    run_command("kubectl get pods -n devops-dashboard")
    run_command("kubectl get deployments -n devops-dashboard")
    run_command("kubectl get services -n devops-dashboard")

def main():
    print("=" * 50)
    print(" DevOps Dashboard Deployment")
    print("=" * 50)

    # Apply all manifests inside the k8s folder
    run_command("kubectl apply -f k8s/")

    print("\nDeployment completed successfully!")

    # Display status of resources
    show_status()

if __name__ == "__main__":
    main()