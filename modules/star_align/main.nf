#!/usr/bin/env nextflow
process STAR_ALIGN {
    label 'process_high'
    container 'ghcr.io/bf528/star:latest'
    publishDir params.outdir, pattern: "*.Log.final.out"

    input:
    path(index_dir) // variable name to reference where input is saved
    tuple val(sample_id), path(reads)

    output:
    tuple val(sample_id),path("${sample_id}.Aligned.out.bam"), emit: bam
    tuple val(sample_id),path("${sample_id}.Log.final.out"), emit: log

    shell:
    """
    STAR --runThreadN $task.cpus \
     --genomeDir $index_dir \
     --readFilesIn ${reads[0]} ${reads[1]} \
     --readFilesCommand zcat \
     --outFileNamePrefix ${sample_id}. \
     --outSAMtype BAM Unsorted
    
    """

}
