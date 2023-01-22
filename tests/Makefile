transcriptomeAlignAnalyze = ../bin/transcriptomeAlignAnalyze

all: test

test: testHES2+A testHES2+A_limits testAll_limits


testHES2+A: output/HES2+A-amplicons.bam
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --target=HES2+A $< output/$@.stats.tsv

testHES2+A_limits: output/HES2+A-amplicons.bam
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBases=1 --maxEndDiff=1 --maxIndelBases=2 --target=HES2+A $< output/$@.stats.tsv

testAll_limits: output/HES2+A-amplicons.bam
	${transcriptomeAlignAnalyze} --readStatsTsv=output/$@.rstats.tsv --maxIndelBases=1 --maxEndDiff=1 --maxIndelBases=2 $< output/$@.stats.tsv


output/HES2+A-amplicons.bam: input/HES2+A-amplicons.sam
	samtools view -O BAM $< >$@
	samtools index $@

mkdirs:
	@mkdir -p output

clean:
	rm -rf output
