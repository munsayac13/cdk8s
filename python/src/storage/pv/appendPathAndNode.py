import os

def AppendToPVFile(distFileName: str, path: str, nodeAffinityHost: str):
    current_directory = os.getcwd() + "/dist"
    with open(current_directory + "/" + distFileName, "a") as file:
        file.write("  local:\n    path: " + path + "\n")
        file.write("  nodeAffinity:\n")
        file.write("    required:\n")
        file.write("      nodeSelectorTerms:\n")
        file.write("      - matchExpressions:\n")
        file.write("        - key: kubernetes.io/hostname\n")
        file.write("          operator: In\n")
        file.write("          values:\n")
        file.write("          - " + nodeAffinityHost + "\n")
        file.close()