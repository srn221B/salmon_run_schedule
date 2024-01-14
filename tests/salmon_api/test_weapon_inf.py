from salmon_api.weapon_inf import WeaponInf, UnknownWeaponError
import pytest

def test_return_inf_if_weapon_is_exists(mocker):
    dummy_data = {'dummy': {'name': 'dummy'}}
    mocker.patch.object(WeaponInf, '_load_data',return_value=dummy_data)
    w = WeaponInf("")
    assert w.get_weapon_data('dummy') == dummy_data['dummy']
    
def test_not_error_if_weapon_is_random(mocker):
    mocker.patch.object(WeaponInf, '_load_data',return_value={})
    w = WeaponInf("")
    assert w.get_weapon_data('ランダム')['name'] == 'ランダム'
    assert w.get_weapon_data('ランダム')['hi'] == 3.5

def test_error_if_not_exists_weapon(mocker):
    dummy_data = {'dummy': {'name': 'dummy'}}
    mocker.patch.object(WeaponInf, '_load_data',return_value=dummy_data)
    w = WeaponInf("")
    with pytest.raises(UnknownWeaponError) as e:
        w.get_weapon_data('hoge')
    assert str(e.value) == 'weapon_name: hoge'