#!/bin/bash
set -beEu -o pipefail

# source this after setting
#   inBam
#   genomeBam
#   outBase
#   filtOps

if [ -z "${inBam}" -o -z "${genomeBam}" -o -z "${outBase}" -o -z "${filtOpts}" ] ; then
    echo "some variable is mssing" >&2
    exit 1
fi

mydir=$(dirname $(which $0))
transcriptomeAlignAnalyze=${mydir}/../../../bin/transcriptomeAlignAnalyze

outTsv=${outBase}.tsv
outTmpTsv=${outTsv}.tmp
outReads=${outBase}.readids

nice ${transcriptomeAlignAnalyze} ${filtOpts} ${inBam} ${outTmpTsv} --filteredReads=${outReads}
mv -f $outTmpTsv $outTsv

outGenomeBam=${outBase}.genome.bam
outGenomeBamTmp=${outGenomeBam}.tmp
nice java -jar ${MED_OPT}/share/picard/picard.jar FilterSamReads \
   I=${genomeBam} O=${outGenomeBamTmp} READ_LIST_FILE=${outReads} FILTER=includeReadList

mv -f ${outGenomeBamTmp} ${outGenomeBam} 
samtools index ${outGenomeBam}


