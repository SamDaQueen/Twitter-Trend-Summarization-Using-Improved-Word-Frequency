import csv
from tf_idf import tf_idf_summarise
from word_freq import word_freq_summarize
from word_freq_improved import word_freq_improved_summarize
from gensim.summarization.summarizer import summarize

text = """BlackBerry smartphones that are being sold by TCL Communication will soon say goodbye to the market as the Chinese manufacturer has announced that it would be parting ways with the Canadian brand as early as August this year. Existing BlackBerry smartphone users would, however, continue to receive after-sales services until August 31, 2022. In 2016, the Shenzhen-based company signed an agreement to manufacture and sell BlackBerry smartphones -- after BlackBerry decided to shift its focus from the smartphone market. The BlackBerry KEYone, BlackBerry KEY2, and BlackBerry Motion are amongst the BlackBerry handsets that are being designed, manufactured, and sold by TCL Communication in major markets. “The support of BlackBerry Limited was an essential element to bringing devices like BlackBerry KEYone, Motion, KEY2, and KEY2 LE to life and we're proud to have partnered with them these past few years on those projects. We do regret to share however that as of August, 31, 2020, TCL Communication will no longer be selling BlackBerry-branded mobile devices,” the company noted in a statement posted on Twitter. In December 2016, TCL Communication signed the licensing deal with BlackBerry to start designing, manufacturing, and selling BlackBerry-branded smartphones in global markets. That announcement was a follow-up of the revelation that the Waterloo-based company made by specifying its plans to outsource the development of BlackBerry phones in September 2016. Through TCL Communication, the smartphone market received Android-based BlackBerry phones, including the BlackBerry KEYone and BlackBerry KEY2 that both featured a physical keyboard alongside a touchscreen panel. The last phone that the Chinese company brought to the market was the BlackBerry KEY 2 LE that was unveiled in August 2018 and debuted in the Indian market in October 2018. TCL Communication in its statement mentioned that it was “blessed enough” to work on BlackBerry smartphones. However, some online reports highlighted that the company was frustrated and was set to give up for quite some time. Existing BlackBerry smartphone users are promised to receive customer service and warranty until August 31, 2022, adding "or for as long as required by local laws where the mobile device was purchased." It is unclear whether the customer service includes any future software updates, though. “The future is bright for both TCL Communication and BlackBerry Limited, and we hope you'll continue to provide support both as we move ahead on our respective paths,” the statement added. Apart from BlackBerry, TCL Communication has other licensed brands on board, including Alcatel and Palm. The latest move isn't likely to impact devices offered by those brands. TCL Communication was notably offering BlackBerry smartphones to select markets, excluding India. In fact, BlackBerry in February 2017 partnered with Optiemus Infracom to specifically produce and sell its Android handsets in India, Sri Lanka, Nepal, and Bangladesh. In Indonesia, it had tied up with BB Merah Putih. Gadgets 360 made several attempts to get clarity from Optiemus Infracom on whether it would continue to manufacture and sell BlackBerry smartphones in its operating markets. The company, however, didn't provide any explicit response until the time of filing this story. The last smartphone that Optiemus Infracom brought to the Indian market was the BlackBerry KEY2 LE. It also launched the BlackBerry Power Wireless Charging Pad in the country in March 2019. Given the ongoing circumstances, the future of BlackBerry smartphones is indeed in the dark. TCL Communication, nevertheless, may leverage its experiences with BlackBerry-branded devices to grow its native presence in the smartphone market. The company is already rumoured to have a foldable smartphone in the works that could debut soon to take on the likes of the Motorola Razr (2019) and Samsung Galaxy Fold."""


print(tf_idf_summarise(text))
print("hello")
print(summarize(text))
print("hello")
print(word_freq_improved_summarize(text))
