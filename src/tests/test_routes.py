import numpy as np
import pytest

from mock import patch


@pytest.fixture
def generate_data_for_tests():
    return {
        "inclinometry": {
            "MD": [0, 1000, 1500],
            "TVD": [0, 1000, 1100]
        },
        "casing": {
            "d": np.random.uniform(0.062, 0.2)
        },
        "tubing": {
            "d": np.random.uniform(0.001, 0.06),
            "h_mes": np.random.uniform(100, 1000)
        },
        "pvt": {
            "wct": np.random.uniform(0, 100),
            "rp": np.random.uniform(0, 500),
            "gamma_oil": np.random.uniform(0.7, 0.9),
            "gamma_gas": np.random.uniform(0.6, 0.8),
            "gamma_wat": np.random.uniform(1, 1.1),
            "t_res": np.random.uniform(30, 200),
            "pb": np.random.uniform(50, 300)
        },
        "p_wh": np.random.uniform(20, 40),
        "geo_grad": np.random.uniform(0, 4),
        "h_res": np.random.uniform(1100, 2000),
    }


def test_calc_model_success(api_client, generate_data_for_tests, sa_session):
    with patch("src.routes.get_session") as mock_session:
        mock_session.return_value = sa_session
        response = api_client.post("vlp/calc",
                                json=generate_data_for_tests)
        assert response.status_code == 200
        result = response.json()
        assert result
        assert result["p_wf"]
        assert result["q_liq"]
