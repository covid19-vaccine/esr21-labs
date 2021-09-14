from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import serum, wb, swab, urine
from .processing_profiles import wb_cmi_processing, hematology_processing
from .processing_profiles import sars_serum_processing, humoral_immunogenicity_processing
from .processing_profiles import sars_pcr_processing, urine_hcg_processing

subject_lab_profile = LabProfile(
    name='esr21_lab_profile',
    requisition_model='esr21_subject.subjectrequisition')

wb_cmi_panel = RequisitionPanel(
    name='wb_cmi',
    verbose_name='WB-CMI',
    aliquot_type=wb,
    processing_profile=wb_cmi_processing)

hematology_panel = RequisitionPanel(
    name='hematology',
    verbose_name='Hematology',
    aliquot_type=wb,
    processing_profile=hematology_processing)

sars_serum_panel = RequisitionPanel(
    name='sars_serum',
    verbose_name='SARS-COV-2 Serology',
    aliquot_type=serum,
    processing_profile=sars_serum_processing)

urine_hcg_panel = RequisitionPanel(
    name='urine_hcg',
    verbose_name='Urine HCG',
    aliquot_type=urine,
    processing_profile=urine_hcg_processing)

humoral_immunogenicity_panel = RequisitionPanel(
    name='humoral_immunogenicity',
    verbose_name='Humoral Immunogenicity',
    aliquot_type=serum,
    processing_profile=humoral_immunogenicity_processing)

sars_pcr_panel = RequisitionPanel(
    name='sars_cov2_pcr',
    verbose_name='SARS-COV-2 PCR',
    aliquot_type=swab,
    processing_profile=sars_pcr_processing)

subject_lab_profile.add_panel(wb_cmi_panel)
subject_lab_profile.add_panel(hematology_panel)
subject_lab_profile.add_panel(sars_serum_panel)
subject_lab_profile.add_panel(humoral_immunogenicity_panel)
subject_lab_profile.add_panel(sars_pcr_panel)
subject_lab_profile.add_panel(urine_hcg_panel)

site_labs.register(subject_lab_profile)
