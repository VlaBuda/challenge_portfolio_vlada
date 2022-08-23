from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button_xpath = "//child::ul[1]/div[1]"
    players_link_xpath = "//child::ul[1]/div[2]"
    language_selector_xpath = "//child::ul[2]/div[1]"
    sign_out_button_xpath = "//child::ul[2]/div[2]"

    players_count_xpath = "//div[contains(text(), 'Players count')]"
    matches_count_xpath = "//div[contains(text(), 'Matches count')]"
    report_count_xpath = "//div[contains(text(), 'Report count')]"
    events_count_xpath = "//div[contains(text(), 'Events count')]"

    scouts_panel_xpath = "//*/div/div/div[2]/h2"
    dev_team_contact_link_xpath = "//*[@target='_blank']"
    shortcuts_xpath = "//h2[contains(text(), 'Shortcuts')]"
    add_player_link_xpath = "//*/div[2]/div/div/a"
    activity_xpath = "//h2[contains(text(), 'Activity')]"

