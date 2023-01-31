transcriptomeAlignAnalyze = ../bin/transcriptomeAlignAnalyze
transcriptomeSummary = ../bin/transcriptomeSummary
transcriptomeFilterCmp = ../bin/transcriptomeFilterCmp
genomeAlignAnalyze = ../bin/genomeAlignAnalyze

ampliconBam = output/HES2+A.amplicon.bam
targetBedGz = output/HES2+A.reads.bed.gz

all: test

test: testHES2+A testHES2+A_limits testAll_limits testRate_limits \
	testSummary testFilterCmp testFilterFirstCmp \
	testHES2+AIntrons

testHES2+A: ${ampliconBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --target=HES2+A $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testHES2+A_limits: ${ampliconBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBases=1 --maxEndsDiff=1 --maxIndelBases=2 --target=HES2+A $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testAll_limits: ${ampliconBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --filteredBam=output/$@.filt.bam --filteredReads=output/$@.filt.ids --maxIndelBases=1 --maxEndsDiff=1 --maxIndelBases=2 $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv
	samtools index output/$@.filt.bam

testRate_limits: ${ampliconBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBaseRate=0.005 --maxEndsDiff=1 --maxIndelBases=2 $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testSummary: mkdirs
	${transcriptomeSummary} expected/testAll_limits.stats.tsv > output/$@.summary.tsv
	diff expected/$@.summary.tsv output/$@.summary.tsv


testFilterCmp: mkdirs
	${transcriptomeFilterCmp} expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

testFilterFirstCmp: mkdirs
	${transcriptomeFilterCmp} --first expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

testHES2+AIntrons: mkdirs ${targetBedGz}
	${genomeAlignAnalyze} input/HES2+A.isoforms.tsv input/HES2+A.targets.bed ${targetBedGz} output/$@.tsv

${ampliconBam}: input/HES2+A.amplicon.sam mkdirs
	samtools view -O BAM $< >$@
	samtools index $@

${targetBedGz}: input/HES2+A.reads.bed mkdirs
	bgzip -c $< > $@
	tabix -p bed $@


mkdirs:
	@mkdir -p output

clean:
	rm -rf output
