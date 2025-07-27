from xsdata.codegen.writer import CodeWriter

from vetis_pydantic_types.xsdata_ext.generator import VetisPydanticGenerator

CodeWriter.register_generator("vetis_pydantic", VetisPydanticGenerator)
