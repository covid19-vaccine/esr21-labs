from edc_lab import ProcessingProfile

from .aliquot_types import wb, serum, swab, urine

wb_cmi_processing = ProcessingProfile(name='wb_cmi', aliquot_type=wb)

hematology_processing = ProcessingProfile(name='hematology', aliquot_type=wb)
# pbmc_pl_process = Process(aliquot_type=pl, aliquot_count=4)
# pbmc_process = Process(aliquot_type=pbmc, aliquot_count=4)
# pbmc_vl_processing.add_processes(pbmc_pl_process, pbmc_process)

sars_serum_processing = ProcessingProfile(name='sars_cov2_serology', aliquot_type=serum)

urine_hcg_processing = ProcessingProfile(name='urine_hcg', aliquot_type=urine)

humoral_immunogenicity_processing = ProcessingProfile(name='humoral_immunogenicity',
                                                      aliquot_type=serum)

sars_pcr_processing = ProcessingProfile(name='sars_cov2_pcr', aliquot_type=swab)
