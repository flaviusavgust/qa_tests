from src.pages.tele2.auto_payments import AutoPaymentsPage


def assert_card_number(driver_fixture, card):
    auto_p = AutoPaymentsPage(driver_fixture)

    first_index = 0
    second_index = 1
    try:
        assert card == auto_p.return_card_number_with_index(index=first_index)
        return first_index

    except AssertionError:
        assert card == auto_p.return_card_number_with_index(index=second_index)
        return second_index
