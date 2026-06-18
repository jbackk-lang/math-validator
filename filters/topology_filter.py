def topology_filter(parsed, singularity_result):
    if singularity_result["status"] == "twist_detected":
        return singularity_result

    if singularity_result["status"] == "hidden_singularity":
        return singularity_result

    return {"status": "clean"}
