from edc_lab import AliquotType

serum = AliquotType(name='Serum', alpha_code='SERUM', numeric_code='06')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

swab = AliquotType(name='Swab', alpha_code='SWAB', numeric_code='03')

urine = AliquotType(name='Urine', alpha_code='URINE', numeric_code='04')

wb.add_derivatives(serum, wb)
