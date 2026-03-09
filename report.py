"""Generate summary reports from datasets."""

from stats import mean, variance, std_dev, normalize


def summary(dataset, label="Dataset"):
    """Print a statistical summary of a dataset."""
    m = mean(dataset)
    v = variance(dataset)
    sd = std_dev(dataset)
    print(f"{label}: mean={m:.2f}, variance={v:.2f}, std_dev={sd:.2f}")
    return {"mean": m, "variance": v, "std_dev": sd}


def compare(dataset_a, dataset_b):
    """Compare two datasets by their normalized distributions."""
    na = normalize(dataset_a)
    nb = normalize(dataset_b)
    return {"a_normalized": na, "b_normalized": nb}


def outliers(dataset, threshold=2.0):
    """Return values more than `threshold` standard deviations from the mean."""
    m = mean(dataset)
    sd = std_dev(dataset)
    result = []
    for n in dataset:
        z = (n - m) / sd
        if abs(z) > threshold:
            result.append(n)
    return result
