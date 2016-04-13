from src.common.models.onewayprice import OneWayPrice
from src.common.models.twowayprice import TwoWayPrice
from src.common.models.routes import Routes

def update_all_oneway(price_for, price_val):
    if (price_for == 'base_price_sedan') :
         OneWayPrice.objects.update(base_price_sedan = price_val)
    if (price_for == 'base_price_suv_7') :
         OneWayPrice.objects.update(base_price_suv_7 = price_val)
    if (price_for == 'base_price_suv_8') :
         OneWayPrice.objects.update(base_price_suv_8 = price_val)
    if (price_for == 'oneway_perkm_sedan') :
         OneWayPrice.objects.update(oneway_perkm_sedan = price_val)
    if (price_for == 'oneway_perkm_suv_7') :
         OneWayPrice.objects.update(oneway_perkm_suv_7 = price_val)
    if (price_for == 'oneway_perkm_suv_8') :
         OneWayPrice.objects.update(oneway_perkm_suv_8 = price_val)

    return True

def update_all_twoway(price_for, price_val):
    if (price_for == 'twoway_perkm_hatchback') :
         TwoWayPrice.objects.update(twoway_perkm_hatchback = price_val)
    if (price_for == 'twoway_perkm_sedan') :
         TwoWayPrice.objects.update(twoway_perkm_sedan = price_val)
    if (price_for == 'twoway_perkm_suv_7') :
         TwoWayPrice.objects.update(twoway_perkm_suv_7 = price_val)
    if (price_for == 'twoway_perkm_suv_8') :
         TwoWayPrice.objects.update(twoway_perkm_suv_8 = price_val)

    return True
