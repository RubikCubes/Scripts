from splinter import Browser

browser = Browser('chrome')


## Load Chrome & Log into Linkedin via command line

browser.visit('https://www.linkedin.com')
browser.fill('session_key','YOUR_EMAIL')
browser.fill('session_password', 'YOUR_PASSWORD')
browser.find_by_css('input[name="submit"]').first.click()
browser.click_link_by_href('/cap/?recruiterEntryPoint=true&trk=nav_responsive_sub_nav_upgrade')
