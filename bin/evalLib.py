def percent(n, total):
    if total == 0:
        return 0.0
    else:
        return round(100 * (n / total), 1)

def rate(n, total):
    if total == 0:
        return 0.0
    else:
        return round((n / total), 3)

supports = ("supported", "likely", "unsupported")
supportRanks = {
    "supported": 1,
    "likely": 2,
    "unsupported": 3,
    "": 4
}

def filterToTranscript(evalDf):
    "get a per-transcript data frame, with maximum support"

    transDf = evalDf[evalDf.plat == "pb"]  # one line per target
    transDf.insert(0, "rank", transDf.category.apply(lambda c: supportRanks[c]))
    transDf = transDf.sort_values(["transcript", "rank"])
    transDf = transDf.drop_duplicates("transcript")

    # drop per-target columns
    dropCols = set(transDf.columns) & set(["rank", "target", "position", "plat", "chain", "chain_in2", "sim_100", "sim_98", "sim_95", "indel_0", "indel_2", "notes"])
    transDf = transDf.drop(dropCols, axis=1)

    return transDf
