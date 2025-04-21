"""
EntityCoreAccessPoint: Unified access to EntityCore resources for BluePyEModel.

This access point provides methods to fetch emodels, ion channels, subcellular model scripts,
extraction configs, and electrophysiological traces from the EntityCore database using its service layer.

Example usage:

    from bluepyemodel.access_point.entitycore_access_point import EntityCoreAccessPoint
    db_session = ...  # SQLAlchemy session
    user_context = ...  # User context as required by EntityCore
    access_point = EntityCoreAccessPoint(db_session=db_session)
    emodel = access_point.get_emodel(emodel_id, user_context=user_context)
    ion_channel = access_point.get_ion_channel(ion_channel_id, user_context=user_context)
    trace = access_point.get_trace(trace_id, user_context=user_context)

See test_entitycore_access_point.py for a runnable test example.

Resource methods:
- get_emodel / get_emodels
- get_ion_channel / get_ion_channels
- get_subcellular_model_script / get_subcellular_model_scripts
- get_extraction_config / get_extraction_configs
- get_trace / get_traces

Each method expects a valid db_session and user_context compatible with the EntityCore API.
"""

import logging
from bluepyemodel.access_point.access_point import DataAccessPoint

# Import EntityCore service and schema for emodels
# (Assumes entitycore is available in PYTHONPATH)
from entitycore.app.service import emodel as entitycore_emodel_service
from entitycore.app.schemas.emodel import EModelRead

logger = logging.getLogger(__name__)

class EntityCoreAccessPoint(DataAccessPoint):
    """
    Access point for BluePyEModel resources using the EntityCore database.
    Implements DataAccessPoint interface.
    """
    def __init__(self, db_session, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_session = db_session  # SQLAlchemy session or similar

    def get_emodel(self, emodel_id, user_context=None):
        """Fetch a single emodel using EntityCore service layer."""
        try:
            # user_context and db_session must be provided as per entitycore's API
            emodel = entitycore_emodel_service.read_one(
                user_context=user_context,
                db=self.db_session,
                id_=emodel_id
            )
            return emodel
        except Exception as e:
            logger.error(f"Failed to fetch emodel {emodel_id} from EntityCore: {e}")
            return None

    def get_emodels(self, pagination_request, emodel_filter, user_context=None):
        """Fetch multiple emodels using EntityCore service layer."""
        try:
            emodels = entitycore_emodel_service.read_many(
                user_context=user_context,
                db=self.db_session,
                pagination_request=pagination_request,
                emodel_filter=emodel_filter,
                with_search=None,
                facets=None
            )
            return emodels
        except Exception as e:
            logger.error(f"Failed to fetch emodels from EntityCore: {e}")
            return []

    def get_ion_channel(self, ion_channel_id, user_context=None):
        """Fetch a single ion channel using EntityCore service layer."""
        try:
            from entitycore.app.service.ion_channel_model import read_one
            ion_channel = read_one(
                user_context=user_context,
                db=self.db_session,
                id_=ion_channel_id
            )
            return ion_channel
        except Exception as e:
            logger.error(f"Failed to fetch ion channel {ion_channel_id} from EntityCore: {e}")
            return None

    def get_ion_channels(self, pagination_request, ion_channel_filter, user_context=None):
        """Fetch multiple ion channels using EntityCore service layer."""
        try:
            from entitycore.app.service.ion_channel_model import read_many
            ion_channels = read_many(
                user_context=user_context,
                db=self.db_session,
                pagination_request=pagination_request,
                ion_channel_filter=ion_channel_filter,
                with_search=None,
                facets=None
            )
            return ion_channels
        except Exception as e:
            logger.error(f"Failed to fetch ion channels from EntityCore: {e}")
            return []

    def get_subcellular_model_script(self, script_id, user_context=None):
        """Fetch a single subcellular model script using EntityCore service layer."""
        try:
            from entitycore.app.service.sub_cellular_model_script import read_one
            script = read_one(
                user_context=user_context,
                db=self.db_session,
                id_=script_id
            )
            return script
        except Exception as e:
            logger.error(f"Failed to fetch subcellular model script {script_id} from EntityCore: {e}")
            return None

    def get_subcellular_model_scripts(self, pagination_request, script_filter, user_context=None):
        """Fetch multiple subcellular model scripts using EntityCore service layer."""
        try:
            from entitycore.app.service.sub_cellular_model_script import read_many
            scripts = read_many(
                user_context=user_context,
                db=self.db_session,
                pagination_request=pagination_request,
                script_filter=script_filter,
                with_search=None,
                facets=None
            )
            return scripts
        except Exception as e:
            logger.error(f"Failed to fetch subcellular model scripts from EntityCore: {e}")
            return []

    def get_extraction_config(self, extraction_config_id, user_context=None):
        """Fetch a single extraction configuration using EntityCore service layer."""
        try:
            from entitycore.app.service.extraction_config import read_one
            extraction_config = read_one(
                user_context=user_context,
                db=self.db_session,
                id_=extraction_config_id
            )
            return extraction_config
        except Exception as e:
            logger.error(f"Failed to fetch extraction config {extraction_config_id} from EntityCore: {e}")
            return None

    def get_extraction_configs(self, pagination_request, extraction_config_filter, user_context=None):
        """Fetch multiple extraction configs using EntityCore service layer."""
        try:
            from entitycore.app.service.extraction_config import read_many
            extraction_configs = read_many(
                user_context=user_context,
                db=self.db_session,
                pagination_request=pagination_request,
                extraction_config_filter=extraction_config_filter,
                with_search=None,
                facets=None
            )
            return extraction_configs
        except Exception as e:
            logger.error(f"Failed to fetch extraction configs from EntityCore: {e}")
            return []

    def get_trace(self, trace_id, user_context=None):
        """Fetch a single trace using EntityCore service layer."""
        try:
            from entitycore.app.service.electrical_cell_recording import read_one
            trace = read_one(
                user_context=user_context,
                db=self.db_session,
                id_=trace_id
            )
            return trace
        except Exception as e:
            logger.error(f"Failed to fetch trace {trace_id} from EntityCore: {e}")
            return None

    def get_traces(self, pagination_request, trace_filter, user_context=None):
        """Fetch multiple traces using EntityCore service layer."""
        try:
            from entitycore.app.service.electrical_cell_recording import read_many
            traces = read_many(
                user_context=user_context,
                db=self.db_session,
                pagination_request=pagination_request,
                trace_filter=trace_filter,
                with_search=None,
                facets=None
            )
            return traces
        except Exception as e:
            logger.error(f"Failed to fetch traces from EntityCore: {e}")
            return []
