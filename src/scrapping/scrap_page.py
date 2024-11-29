import time

from src.services.Driver import Driver


driver = Driver(
    url="https://www.grailed.com/sold",
    num_of_iterations=5,
    sleep_time=10
)

with driver:
    driver.open()
    driver.handle_pop_up("onetrust-accept-btn-handler")
    driver.navigate_to_login(
        login_locator="global-header-login-btn",
        login_by_email_locator='button[data-cy="login-with-email"]'
    )
    driver.login(
        username_locator="email",
        password_locator="password"
    )


