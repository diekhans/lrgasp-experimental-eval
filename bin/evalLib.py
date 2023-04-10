def percent(n, total, places=1):
    if total == 0:
        return 0.0
    else:
        return round(100 * (n / total), places)

def rate(n, total, places=3):
    if total == 0:
        return 0.0
    else:
        return round((n / total), places)

def rateFmt(n, total, places=3):
    if total == 0:
        return "0.0"
    else:
        r = n / total
        return f"{r:.{places}g}"

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

def splitBySquantiCategory(transDf):
    knownDf = transDf[transDf.transcript.str.startswith('FSM')]  # FSM
    novelDf = transDf[transDf.transcript.str.startswith('NIC')
                      + transDf.transcript.str.startswith('NNC')]  # NIC/NNC
    ismDf = transDf[transDf.transcript.str.startswith('ISM')]  # FSM
    if len(knownDf) + len(novelDf) + len(ismDf) != len(transDf):
        raise Exception("logic error splitting transcripts")

    return knownDf, novelDf, ismDf

def splitBySupport(transDf):
    supportedDf = transDf[transDf.category != "unsupported"]
    unsupportedDf = transDf[transDf.category == "unsupported"]
    assert (len(supportedDf) + len(unsupportedDf)) == len(transDf)
    return supportedDf, unsupportedDf
