# Task 1: Software configuration
## Subtask1: Why did I choose to participate in the challenge portfolio?
Maybe it will sound a little strange, but I want to be involved in the creation of quality software. 
It is, you know, something like a mission that you feel.I set myself the goal of learning automation. 
I have already studied manual testing, had some practice. 
And now I'm interested in improving my knowledge, bringing it to a new level.
My expectations are new information that I will be able to use, as well as try myself in an internship (if I am chosen).

# Task 2: Selectors
## Subtask 1: Searching for selectors on the login page. List all the elements that are on the login page.

Selectors for Scouts Panel
1.//child::div/h5
2.//h5

Selectors for Login
1.//input[@id="login"] 
2.//*[@name="login"] 
3.//child::div/input
 
Selectors for password
1.[name=password]
2.//*[@name="password"] 
3.//input[@id="password"] 
 
Selectors for remind password
1.//*[text()="Remind password"]
2.//a
3.//child::div/a

Selectors for language dropdown (English)
1.//input[@value="en"]
2.[value=en]
3.//input[@class="MuiSelect-nativeInput"]
 
Selectors for language dropdown (Polish)
1.[value=pl]
2.//input[@value="pl"]
3.//input[@class="MuiSelect-nativeInput"]
 
Selectors for button
1.//*[@type="submit"]
2.//child::div/button
