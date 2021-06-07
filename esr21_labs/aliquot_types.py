from edc_lab import AliquotType

serum = AliquotType(name='Serum', alpha_code='SERUM', numeric_code='06')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

wb.add_derivatives(serum, wb)
