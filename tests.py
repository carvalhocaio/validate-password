import pytest
import json
from flask.testing import FlaskClient
from app import server


@pytest.fixture
def client():
    return server.test_client()


def test_verify_password_return_a_message_if_the_password_is_not_informed_in_the_body_of_request(
    client: FlaskClient,
):
    response = client.post(
        "/verify", content_type="application/json", data=json.dumps({})
    )

    assert response.status_code == 422
    assert json.loads(response.data.decode("utf-8")) == [
        {
            "loc": ["password"],
            "msg": "field required",
            "type": "value_error.missing",
        }
    ]


def test_verify_password_without_rules(client: FlaskClient):
    response = client.post(
        "/verify",
        content_type="application/json",
        data=json.dumps({"password": "TestSenhaForte!123&"}),
    )

    assert response.status_code == 200
    assert json.loads(response.data.decode("utf-8")) == {"noMatch": [], "verify": True}


def test_verify_password_with_all_rules_and_not_pass(client: FlaskClient):
    response = client.post(
        "/verify",
        content_type="application/json",
        data=json.dumps(
            {
                "password": "password",
                "rules": [
                    {"rule": "minSize", "value": 12},
                    {"rule": "minUppercase", "value": 5},
                    {"rule": "minLowercase", "value": 9},
                    {"rule": "minDigit", "value": 4},
                    {"rule": "minSpecialChars", "value": 2}
                ],
            }
        ),
    )

    assert response.status_code == 200
    assert json.loads(response.data.decode("utf-8")) == {
        "noMatch": [
            "minSize",
            "minUppercase",
            "minLowercase",
            "minDigit",
            "minSpecialChars",
        ],
        "verify": False,
    }


def test_verify_password_with_all_rules_and_pass(client: FlaskClient):
    response = client.post(
        "/verify",
        content_type="application/json",
        data=json.dumps(
            {
                "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
                "rules": [
                    {"rule": "minSize", "value": 12},
                    {"rule": "minUppercase", "value": 5},
                    {"rule": "minLowercase", "value": 9},
                    {"rule": "minDigit", "value": 4},
                    {"rule": "minSpecialChars", "value": 2},
                ],
            }
        ),
    )

    assert response.status_code == 200
    assert json.loads(response.data.decode("utf-8")) == {"noMatch": [], "verify": True}


def test_verify_password_with_each_rule_and_not_pass(client: FlaskClient):
    input_data = [
        {"password": "password", "rules": [{"rule": "minSize", "value": 12}]},
        {"password": "password", "rules": [{"rule": "minUppercase", "value": 5}]},
        {"password": "PASSWORD", "rules": [{"rule": "minLowercase", "value": 5}]},
        {"password": "password", "rules": [{"rule": "minDigit", "value": 2}]},
        {"password": "password", "rules": [{"rule": "minSpecialChars", "value": 3}]},
    ]

    output_data = [
        {"noMatch": ["minSize"], "verify": False},
        {"noMatch": ["minUppercase"], "verify": False},
        {"noMatch": ["minLowercase"], "verify": False},
        {"noMatch": ["minDigit"], "verify": False},
        {"noMatch": ["minSpecialChars"], "verify": False},
    ]

    for _, (input_data, output_data) in enumerate(
        zip(input_data, output_data), start=1
    ):
        response = client.post(
            "/verify", content_type="application/json", data=json.dumps(input_data)
        )

        assert response.status_code == 200
        assert json.loads(response.data.decode("utf-8")) == output_data


def test_verify_password_with_each_rule_and_pass(client: FlaskClient):
    input_data = [
        {
            "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
            "rules": [{"rule": "minSize", "value": 12}],
        },
        {
            "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
            "rules": [{"rule": "minUppercase", "value": 5}],
        },
        {
            "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
            "rules": [{"rule": "minLowercase", "value": 5}],
        },
        {
            "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
            "rules": [{"rule": "minDigit", "value": 2}],
        },
        {
            "password": "@h(i+i_9*#50vC4@#5A-v$o)_G)vYr)!k@6rS",
            "rules": [{"rule": "minSpecialChars", "value": 3}],
        },
    ]

    output_data = [
        {"noMatch": [], "verify": True},
        {"noMatch": [], "verify": True},
        {"noMatch": [], "verify": True},
        {"noMatch": [], "verify": True},
        {"noMatch": [], "verify": True},
    ]

    for _, (input_data, output_data) in enumerate(
        zip(input_data, output_data), start=1
    ):
        response = client.post(
            "/verify", content_type="application/json", data=json.dumps(input_data)
        )

        assert response.status_code == 200
        assert json.loads(response.data.decode("utf-8")) == output_data
