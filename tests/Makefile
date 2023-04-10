transcriptomeAlignAnalyze = ../bin/transcriptomeAlignAnalyze
transcriptomeSummary = ../bin/transcriptomeSummary
transcriptomeFilterCmp = ../bin/transcriptomeFilterCmp
genomeAlignAnalyze = ../bin/genomeAlignAnalyze
summarizeSupport = ../bin/summarizeSupport
paperEvalStats = ../bin/paperEvalStats
squantiSummary = ../bin/squantiSummary

hes2AmpliconsBam = output/HES2+A.amplicon.bam
ankmy2AmplicaonBam = output/ANKMY2+1.amplicon
hes2GenomeBam = output/HES2+A.genome.bam
alg6GenomeBam = output/ALG6+A.genome.bam

all: test

test: transcriptomeTests genomeTests otherTests paperEvalTests squantiSummaryTests

transcriptomeTests: testHES2+A testHES2+A_limits testAll_limits testRate_limits \
	testSimilarity99 testSimilarity95 testANKMY2Sim \
	testANKMY2Indel testANKMY2Strand 

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

# This didn't find a perfect match
testANKMY2Sim: ${ankmy2AmplicaonBam}
	${transcriptomeAlignAnalyze} --minSimilarity=0.10 $< output/pb-$@.stats.tsv
	diff expected/pb-$@.stats.tsv output/pb-$@.stats.tsv

testANKMY2Indel: ${ankmy2AmplicaonBam}
	${transcriptomeAlignAnalyze} --maxIndelBases=10 $< output/pb-$@.stats.tsv
	diff expected/pb-$@.stats.tsv output/pb-$@.stats.tsv

testANKMY2Strand: ${ankmy2AmplicaonBam}
	${transcriptomeAlignAnalyze} --filterStrand --maxIndelBases=5 $< output/pb-$@.stats.tsv
	diff expected/pb-$@.stats.tsv output/pb-$@.stats.tsv

otherTests: testSummary testFilterCmp testFilterFirstCmp testSummarizeSupport

testSummary: mkdirs
	${transcriptomeSummary} expected/testAll_limits.stats.tsv > output/$@.summary.tsv
	diff expected/$@.summary.tsv output/$@.summary.tsv


testFilterCmp: mkdirs
	${transcriptomeFilterCmp} expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

testFilterFirstCmp: mkdirs
	${transcriptomeFilterCmp} --first expected/testAll_limits.stats.tsv expected/testHES2+A.stats.tsv > output/$@.cmp.tsv
	diff expected/$@.cmp.tsv output/$@.cmp.tsv

genomeTests: testHES2+A_introns testALG6+1_introns \
	testHES2+A_introns_indel

testHES2+A_introns: mkdirs ${hes2GenomeBam}
	${genomeAlignAnalyze} input/HES2+A.isoforms.tsv input/HES2+A.amplicon.bed ${hes2GenomeBam} output/$@.tsv --supportBam=output/$@.support.bam
	samtools view output/$@.support.bam >output/$@.support.sam
	diff expected/$@.tsv output/$@.tsv
	diff expected/$@.support.sam output/$@.support.sam

testHES2+A_introns_indel: mkdirs ${hes2GenomeBam}
	${genomeAlignAnalyze} --maxIndelBases=2 input/HES2+A.isoforms.tsv input/HES2+A.amplicon.bed ${hes2GenomeBam} output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

testALG6+1_introns: mkdirs ${alg6GenomeBam}
	${genomeAlignAnalyze} input/ALG6+1.isoforms.tsv input/ALG6+1.amplicon.bed ${alg6GenomeBam} output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

testSummarizeSupport: mkdirs
	cp expected/testHES2+A_introns.tsv output/pb-genome.tsv
	${summarizeSupport} similarity input/HES2+A.isoforms.tsv --genomeStatsTsv=output/pb-genome.tsv expected/pb-testSimilarity95.stats.tsv expected/pb-testSimilarity99.stats.tsv >output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

${hes2AmpliconsBam}: input/HES2+A.amplicon.sam | mkdirs
	samtools view -O BAM $< >$@
	samtools index $@

${ankmy2AmplicaonBam}: input/ANKMY2+1.amplicon.sam | mkdirs
	samtools view -O BAM $< >$@
	samtools index $@

${hes2GenomeBam}: input/HES2+A.genome.sam | mkdirs
	samtools view -b $< > $@
	samtools index $@

${alg6GenomeBam}: input/ALG6+1.genome.sam | mkdirs
	samtools view -b $< > $@
	samtools index $@

paperEvalTests: testPaperEvalWtc11

testPaperEvalWtc11: mkdirs
	${paperEvalStats} input/wtc11.evaluation.part.tsv output/$@.tsv
	diff expected/$@.tsv output/$@.tsv

squantiSummaryTests: testSquantiSummary1

testSquantiSummary1: mkdirs
	${squantiSummary} input/WTC11.pa.part.csv input/wtc11.evaluation.part.tsv input/wtc11.id_ujc.part.tsv output/$@.tsv
	diff expected/$@.tsv output/$@.tsv


mkdirs:
	@mkdir -p output

clean:
	rm -rf output
