transcriptomeAlignAnalyze = ../bin/transcriptomeAlignAnalyze
transcriptomeSummary = ../bin/transcriptomeSummary
transcriptomeFilterCmp = ../bin/transcriptomeFilterCmp
genomeAlignAnalyze = ../bin/genomeAlignAnalyze
summarizeSupport = ../bin/summarizeSupport

hes2AmpliconsBam = output/HES2+A.amplicon.bam
hes2GenomeBam = output/HES2+A.genome.bam
alg6GenomeBam = output/ALG6+A.genome.bam

all: test

test: testHES2+A testHES2+A_limits testAll_limits testRate_limits \
	testSimilarity99 testSimilarity95 \
	testSummary testFilterCmp testFilterFirstCmp \
	testHES2+A_introns testALG6+1_introns \
	testHES2+A_introns_indel \
	testSummarizeSupport

testHES2+A: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --target=HES2+A $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testHES2+A_limits: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBases=1 --maxEndsDiff=1 --maxIndelBases=2 --target=HES2+A $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testAll_limits: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --filteredBam=output/$@.filt.bam --filteredReads=output/$@.filt.ids --maxIndelBases=1 --maxEndsDiff=1 --maxIndelBases=2 $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv
	samtools index output/$@.filt.bam

testRate_limits: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBaseRate=0.005 --maxEndsDiff=1 --maxIndelBases=2 $< output/$@.stats.tsv
	diff expected/$@.stats.tsv output/$@.stats.tsv

testSimilarity99: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --minSimilarity=0.99 $< output/pb-$@.stats.tsv
	diff expected/pb-$@.stats.tsv output/pb-$@.stats.tsv

testSimilarity95: ${hes2AmpliconsBam}
	${transcriptomeAlignAnalyze} --minSimilarity=0.95 $< output/pb-$@.stats.tsv
	diff expected/pb-$@.stats.tsv output/pb-$@.stats.tsv

testSummary: mkdirs
	${transcriptomeSummary} expected/testAll_limits.stats.tsv > output/$@.summary.tsv
	diff expected/$@.summary.tsv output/$@.summary.tsv


testFilterCmp: mkdirs
	${transcriptomeFilterCmp} expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

testFilterFirstCmp: mkdirs
	${transcriptomeFilterCmp} --first expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

testHES2+A_introns: mkdirs ${hes2GenomeBam}
	${genomeAlignAnalyze} input/HES2+A.isoforms.tsv input/HES2+A.targets.bed ${hes2GenomeBam} output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

testHES2+A_introns_indel: mkdirs ${hes2GenomeBam}
	${genomeAlignAnalyze} --maxIndelBases=2 input/HES2+A.isoforms.tsv input/HES2+A.targets.bed ${hes2GenomeBam} output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

testALG6+1_introns: mkdirs ${alg6GenomeBam}
	${genomeAlignAnalyze} input/ALG6+1.isoforms.tsv input/ALG6+1.targets.bed ${alg6GenomeBam} output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

testSummarizeSupport: mkdirs
	cp expected/testHES2+A_introns.tsv output/pb-genome.tsv
	${summarizeSupport} similarity input/HES2+A.isoforms.tsv --genomeStatsTsv=output/pb-genome.tsv expected/pb-testSimilarity95.stats.tsv expected/pb-testSimilarity99.stats.tsv >output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

${hes2AmpliconsBam}: input/HES2+A.amplicon.sam mkdirs
	samtools view -O BAM $< >$@
	samtools index $@

${hes2GenomeBam}: input/HES2+A.genome.sam mkdirs
	samtools view -b $< > $@
	samtools index $@

${alg6GenomeBam}: input/ALG6+1.genome.sam mkdirs
	samtools view -b $< > $@
	samtools index $@

mkdirs:
	@mkdir -p output

clean:
	rm -rf output
