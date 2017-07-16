#-*- coding: utf-8 -*-

# https://genome.ucsc.edu/FAQ/FAQformat.html
BED12_FIELDS = ['chrom', 'start', 'end',
                'name', 'score', 'strand',
                'thickStart', 'thickEnd', 'rgb',
                'blockCount', 'blockSizes', 'blockStarts']
BED_FIELDS = BED12_FIELDS[:6]

BEDPE_FIELDS = ['chrom1', 'start1', 'end1',
                'chrom2', 'start2', 'end2',
                'name', 'score', 'strand1', 'strand2']
GFF_FIELDS = ['chrom', 'source', 'feature', 'start', 'end',
              'score', 'strand', 'frame', 'attributes']

PGSNP_FIELDS = ['chrom', 'start', 'end', 'name',
                'alleleCount', 'alleleFreq', 'alleleScores']
BEDRNAELEMENTS_FIELDS = ['chrom', 'start', 'end', 'name', 'score', 'strand',
              'level', 'signif', 'score2']
NARROWPEAK_FIELDS = ['chrom', 'start', 'end', 'name', 'score', 'strand',
                     'fc', '-log10p', '-log10q', 'relSummit']
BROADPEAK_FIELDS = ['chrom', 'start', 'end', 'name', 'score', 'strand',
                     'fc', '-log10p', '-log10q']
GAPPEDPEAK_FIELDS = ['chrom', 'start', 'end', 'name', 'score', 'strand',
                     'thickStart', 'thickEnd', 'rgb',
                     'blockCount', 'blockSizes', 'blockStarts',
                     'fc', '-log10p', '-log10q']
GAP_FIELDS = ['bin', 
              'chrom', 'start', 'end', 
              'ix', 'n', 
              'length', 'type', 'bridge']

# http://ga4gh.org/#/fileformats-team
BAM_FIELDS = ['QNAME', 'FLAG', 'RNAME', 'POS', 'MAPQ', 'CIGAR',
              'RNEXT', 'PNEXT', 'TLEN', 'SEQ', 'QUAL', 'TAGs']
VCF_FIELDS = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

SCHEMAS = {
    'bed': BED_FIELDS,
    'bedGraph': BED_FIELDS[:3],
    'bed3': BED_FIELDS[:3],
    'bed4': BED_FIELDS[:4],
    'bed5': BED_FIELDS[:5],
    'bed6': BED_FIELDS,
    'bed9': BED12_FIELDS[:9],
    'bed12': BED12_FIELDS,
    'gff': GFF_FIELDS,
    'gtf': GFF_FIELDS,
    'bedRnaElements': BEDRNAELEMENTS_FIELDS,
    'narrowPeak': NARROWPEAK_FIELDS,
    'broadPeak': BROADPEAK_FIELDS,
    'gappedPeak': GAPPEDPEAK_FIELDS,
    'bam': BAM_FIELDS,
    'vcf': VCF_FIELDS,
}