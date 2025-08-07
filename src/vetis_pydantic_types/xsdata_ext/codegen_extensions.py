from vetis_pydantic_types.xsdata_ext.insert_classes import VersionStatus

URL_TO_EXTENSIONS_SETTINGS = {
    'http://api.vetrf.ru/schema/cdm/base': {
        'insert_classes': [
            VersionStatus,
        ],
        'change_annotations': {
            'GenericVersioningEntity.status': 'VersionStatus',
        },
    },
}
