# from src import dsc_engine
# import pytest
# from eth.codecs.abi.exceptions import EncodeError

# def test_reverts_if_token_lengths_are_different(dsc, eth_usd, btc_usd, weth, wbtc):
#     with pytest.raises(EncodeError):
#         dsc_engine.deploy([wbtc, weth, weth], [eth_usd, btc_usd], dsc.address)

from src import dsc_engine
import pytest
from eth.codecs.abi.exceptions import EncodeError
from tests.conftest import COLLATERAL_AMOUNT
import boa
def test_reverts_if_token_lengths_are_different(dsc, btc_usd, weth, wbtc):
    with pytest.raises(EncodeError):
        dsc_engine.deploy(
            [wbtc, weth, weth],   # length = 3 ❌
            [btc_usd, btc_usd],   # length = 2 ✅
            dsc.address
        )

def test_reverts_if_collateral_zero(some_user, weth, dsce):
    with boa.env.prank(some_user):
        weth.approve(dsce, COLLATERAL_AMOUNT)
        with boa.reverts():
            dsce.deposit_collateral(weth, 0)