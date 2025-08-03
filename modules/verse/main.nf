#!/usr/bin/env nextflow
process VERSE {
    label "process_simple"
    container 'ghcr.io/bf528/verse:latest'
    publishDir params.outdir, mode: 'copy'

    input:
        tuple val(meta), path(bam)  // Input is a BAM file
        path(gtf)                   // and a GTF annotation file

    output:
        tuple val(meta), path("*.exon.txt"), emit: counts

    shell:
        """
        verse -S -a $gtf -o $meta $bam
        """
    
}