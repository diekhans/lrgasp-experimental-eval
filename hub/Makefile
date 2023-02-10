ROOT = ..

hubUrl = https://hgwdev.gi.ucsc.edu/~markd/lrgasp/experimental-eval/hub/hub.txt

twoBit_hg38 = https://hgdownload.soe.ucsc.edu/gbdb/hg38/hg38.2bit
twoBit_manatee = ../../primers/primer-design/data/manatee/manatee.2bit

genomes = hg38 manatee

all: 
	hubCheck ${hubUrl}

build: ${genomes:%=build_%}
build_%:
	${MAKE} genome_build genome=$*

clean: ${genomes:%=clean_%}
clean_%:
	${MAKE} genome_clean genome=$*


##
# recurisve  genome=
##
twoBit = ${twoBit_${genome}}

bigBeds =

genome_build: 

genome_clean:

