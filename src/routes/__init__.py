from fastapi import APIRouter, Depends
from src.db import get_session
from src.models.models import VlpCalcRequest, VlpCalcResponse
from src.routes.queries import save_init_data, save_vlp_data, get_check_well_data_exists, get_check_vlp_exists
from src.utils import get_dict_hash


main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
async def calc_vlp(vlp_in: VlpCalcRequest, session = Depends(get_session)):
    """Расчёт VLP по исходным данным и сохранение в Базу"""
    # функция считающая VLP
    from src.calculations.vlp import calc_vlp as vlp_calculation  # noqa

    vlp_in_dict = vlp_in.dict()
    well_data_id = get_dict_hash(vlp_in_dict)
    vlp = None


    if not get_check_well_data_exists(session, well_data_id):
        save_init_data(session, vlp_in_dict, well_data_id)

    vlp = get_check_vlp_exists(session, well_data_id)
    if not vlp:
        vlp = await vlp_calculation(**vlp_in_dict)
        save_vlp_data(session, vlp, well_data_id)

    return vlp
