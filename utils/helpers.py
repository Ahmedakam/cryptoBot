import random
import qrcode
from io import BytesIO
import string
import html
import re
from datetime import datetime, timedelta, timezone

def generate_qr_code_image(pay_address, pay_amount, pay_currency):
    # تنسيق البيانات لرمز QR. يمكن أن يختلف هذا قليلاً حسب العملة
    # على سبيل المثال، لـ USDT (TRC20)، قد يكون مجرد العنوان
    # لـ BTC، قد يكون bitcoin:{address}?amount={amount}
    # هنا نفترض أننا نستخدم عنوان الدفع والمبلغ كنص عادي
    qr_data = f"{pay_address}"
UQARIQeRt55gDYdCp96da0wV9_sFnpg1m2rEHLXw9HTdu9LC
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # حفظ الصورة في الذاكرة وإرجاعها
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def price_change(old_price, new_price):
    return ((new_price - old_price) / old_price) * 100

def format_percentage(value):
    return f"{value:.2f}%"


def generate_order_id(prefix="sub", user_id=None, plan_type=None, duration=None):
    rand_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    ts = datetime.now().strftime('%Y%m%d%H%M%S')
    return f"{prefix}_{user_id}_{plan_type}_{duration}_{rand_part}_{ts}"



def is_payment_expired(created_at, timeout_minutes=20):
    # Assume created_at is UTC and convert it to a timezone-aware datetime object
    created = datetime.fromisoformat(created_at).replace(tzinfo=timezone.utc)
    expiry_time = created + timedelta(minutes=timeout_minutes)
    current_time = datetime.now(timezone.utc) # Get current time in UTC
    print(f"DEBUG: Payment created at: {created}, Expiry time: {expiry_time}, Current time: {current_time}")
    return current_time > expiry_time


def strip_html_tags_and_unescape_entities(text: str) -> str:
    TAG_RE = re.compile(r'<[^>]+>')
    """
    يزيل علامات HTML ويفك تشفير كيانات HTML من النص.
    """
    if not isinstance(text, str):
        return ""
    # فك تشفير كيانات HTML أولاً
    unescaped_text = html.unescape(text)
    # ثم إزالة علامات HTML
    return TAG_RE.sub('', unescaped_text)

def extract_network_from_currency(pay_currency: str) -> str:
    """
    Extracts the network from a given pay_currency string.
    """
    pay_currency = pay_currency.lower()
    if pay_currency.endswith('bsc'):
        return 'Binance Smart Chain (BSC)'
    elif pay_currency.endswith('ton'):
        return 'TON'
    # Add more network extractions as needed
    return 'N/A' # Default if no specific network is identified

MESSAGES = {
    'ar': {
        'welcome': """
        🎉  أهلاً وسهلاً بك في بوت اشتراكات قناة OWL CAB🦉!

        😍يسعدنا انضمامك إلى مجموعة مستخدمي القناة الذكية المختصة بسوق الكريبتو لمساعدتك في متابعة سوق الكريبتو بسهولة ويُسر.
        يمكنك الحصول الان على تجربتك المجانية والتي تتيح لك:

        تجربة جميع الميزات الحصرية لـمدة محدودة بدون أي التزام!

        متابعة اخر اخبار سوق العملات الرقمية من اكثر من مصدر موثوق📰.

        تحليل للاخبار بالذكاء الاصطناعي AI 🤖

        📊تلقي تنبيهات للعملات والأسعار، واكتشاف فرص التداول اللحظية.

        روابط مباشرة للعملات عبر البرنامج الشهير TradingView🔗.

        ملاحظات هامة⚠️:

        تستطيع الاستفادة من جميع الخدمات خلال فترة التجربة المجانية. عند انتهائها، سيطلب منك الاشتراك لمواصلة استخدام الميزات المتقدمة.

        لكل مستخدم تجربة مجانية واحدة فقط، بعدها يمكنك اختيار الباقة المناسبة لك.

        <b>(البوت يعرض معلومات فقط ولا يقدم نصائح استثمارية أو يضمن تحقيق أرباح أو تجنب خسائر. جميع قرارات التداول والاستثمار تقع على عاتق المستخدم وحده).</b>

        وسائل الدفع :
            عملات رقمية :
                - USDT TON

       
        فيزا / ماستر كارد (قريبَا ⌛❤️)


        إذا واجهتك أي مشكلة أو استفسار، تواصل معنا عبر حسابات. القناة على وسائل التواصل الاجتماعي:
        - تويتر  (X حالياَ): <a href="https://x.com/OwlBot_72?t=vw5b-FfKvAxBe1ND1GenXA&s=09">@OWL_CAB</a>
        - تيك توك : <a href="https://www.tiktok.com/@owl.cab?_r=1&_t=ZS-91SE1Qyqi51">owl.cab</a>
        - يوتيوب : <a href="https://youtube.com/@owlcab_7?si=R1ujFOV2sqEBuDb5">owlcab_7</a>
        - انستجرام : <a href="https://www.instagram.com/owlcab7?igsh=MTBrcnd4ODVnNTVpYw==">owlcab7</a>

        🚀 ابدأ تجربتك الآن واستكشف مميزات البوت بالكامل قبل انتهاء الفترة المجانية!

        نتمنى لك رحلة تداول ناجحة وخبرة تحليل متميزة معنا 🌟

        صنع في السعودية 🇸🇦💚

        – <a href="https://wesamlt.netlify.app/">مبرمج</a> OWL CAB 🦉
        """,
        'commands_prompt': "يمكنك استخدام الأوامر التالية:",
        'subscribe_plans_prompt': '📦 اختر خطة الاشتراك:',
        'free_trial_activated': "🎉 لقد تم تفعيل التجربة المجانية الخاصة بك!\nرابط القناة: {channel_link}",
        'already_subscribed': "⚠️ أنت لديك اشتراك فعال بالفعل!",
        'payment_details_prompt': "💰 <b>تفاصيل الدفع:</b>\n"
                                  "⚠️  أرسل المبلغ ((بالضبط)) -وإلا قد تحدث مشاكل في عملية الدفع- إلى العنوان الموجود على الشبكة المطلوبة تحديداَ في الرابط أدناه\n"
                                  "\n ©️ معرف الطلب : {order_id}\n"
                                  "\n<b>💰 المبلغ المطلوب: {price_amount} {price_currency}\n</b>"
                                  "\n<b>💳 عنوان المحفظة المطلوب التحويل لها: {pay_address}\n</b>"
                                  "\n<b>🌐 الشبكة: {network}\n</b>"
                                  "✅ سيتم ارسال رابط القناة و تفعيل اشتراكك تلقائياً بعد التأكيد (1-10 دقائق)\n"
                                  "🔍للتحقق من حالة الدفع: /check_payment",
        'pay_now_button': "💳 ادفع الآن",
        'qr_code_caption': "امسح رمز QR هذا لنسخ عنوان المحفظة:  {pay_address} ",
        'no_pending_payment': "لا توجد عملية دفع معلقة للتحقق منها.",
        'payment_details_not_found': "لم يتم العثور على تفاصيل الدفع المعلقة.",
        'payment_expired': "⏳ انتهت صلاحية عملية الدفع هذه (أكثر من 20 دقيقة).\nيرجى اختيار الاشتراك من جديد.",
        'payment_successful': "✅🥳🤩 تم تأكيد الدفع بنجاح! تم تفعيل الاشتراك. \n معرف الطلب: {order_id},\n المدة: {duration} شهر,\n رابط القناة: {channel_link}.\n===========\n (✅🥳🤩Payment confirmed successfully! Your subscription is now active.\n Order ID: {order_id},\n Duration: {duration} Month,\n Channel Link: {channel_link}.)",   
        'payment_failed_cancelled': "❌ فشل أو إلغاء الدفع. يرجى المحاولة مرة أخرى. (Payment failed or cancelled. Please try again.)",
        'payment_pending': "⏳ لا تزال عملية الدفع الخاصة بك معلقة. معرف الطلب: {order_id}\n تاكد من دفع المبلغ المطلوب الى المحفظة الاتية: {pay_address}\nسنقوم بإعلامك بمجرد تأكيد الدفع.",
        'already_have_pending_payment': "⚠️ لديك دفع معلق نشط بالفعل. معرف الطلب: {order_id}\n يرجى إتمام الدفع عبر عنوان المحفظة الموجود أدناه:\n{pay_address}",
        'help_message': "أهلاً بك في بوت OWL CAB Subscriptions! إليك الأوامر التي يمكنك استخدامها:\n\n"
                        "/start - لبدء التفاعل مع البوت.\n"
                        "/subscribe - لاشتراك في خدمة OWL CAB.\n"
                        "/check_payment - للتحقق من حالة دفعك الأخير.\n"
                        "/help - لعرض هذه الرسالة المساعدة.\n",
        'choose_language': "الرجاء اختيار لغتك المفضلة:",
        'arabic_button': "🇸🇦 العربية",
        'english_button': "🇬🇧 English",
        'language_set_to': "تم تعيين اللغة إلى العربية.",
        'subscribe_command': 'subscribe',
        'check_payment_command': 'check_payment',
        'help_command': 'help',
        'one_day_trial': "1 يوم تجريبي مجانا ",
        'one_month_subscription': "1 شهر",
        'three_month_subscription': "3 أشهر",
        'six_month_subscription': "6 أشهر",
    },
    'en': {
        'welcome': """
🎉 Welcome to OWL CAB🦉 Subscription Bot!

😍 We are delighted to have you join the smart channel user group specialized in the crypto market to help you follow the crypto market with ease.
You can now get your first free trial, which allows you to:

Experience all exclusive features for a limited time without any commitment!

Follow the latest crypto market news from more than one reliable source📰.

AI analysis of news 🤖

📊 Receive advanced alerts for currencies and prices, and discover instant trading opportunities.

Direct links to currencies via the famous TradingView program🔗.

Important notes⚠️:

You can benefit from all services during the free trial period. Upon its expiration, you will be asked to subscribe to continue using the advanced features.

Each user gets only one free trial, after which you can choose the appropriate package for you.

<b>(The bot displays information only and does not provide investment advice or guarantee profits or avoid losses. All trading and investment decisions are the sole responsibility of the user).</b>

💳 Payments :
    cryptocurrencies :
        - USDT TON

visa / master card (soon ⌛❤️)

If you encounter any problem or inquiry, contact us via our Social Media Accounts of OWL CAB:

        - X (Previously known as Twitter) : <a href="https://x.com/OwlBot_72?t=vw5b-FfKvAxBe1ND1GenXA&s=09">@OWL_CAB</a>
        - TikTok : <a href="https://www.tiktok.com/@owl.cab?_r=1&_t=ZS-91SE1Qyqi51">owl.cab</a>
        - YouTube : <a href="https://youtube.com/@owlcab_7?si=R1ujFOV2sqEBuDb5">owlcab_7</a>
        - Instagram : <a href="https://www.instagram.com/owlcab7?igsh=MTBrcnd4ODVnNTVpYw==">owlcab7</a>

🚀 Start your experience now and explore the bot's full features before the free period ends!

We wish you a successful trading journey and an excellent analysis experience with us 🌟

Made in Saudi Arabia 🇸🇦💚

– OWL CAB 🦉 <a href="https://wesamlt.netlify.app/">dev.</a>
""",
        'commands_prompt': "You can use the following commands:",
        'subscribe_plans_prompt': '📦 Choose a subscription plan:',
        'free_trial_activated': "🎉 Your free trial has been activated!\nChannel Link: {channel_link}",
        'already_subscribed': "⚠️ You already have an active subscription!",
        'payment_details_prompt': "💰 <b>Payment Details:</b>\n"
                                  "⚠️ Send the amount ((exactly)) - otherwise, problems may occur in the payment process - to the address and network specified in the link below\n"
                                  "\n©️ Order ID: {order_id}\n"
                                  "\n<b>💰 Price Amount: {price_amount} {price_currency}\n</b>"
                                  "\n<b>💳 Pay Address: {pay_address}\n</b>"
                                  "\n<b>🌐 Network: {network}\n</b>"
                                  "✅ Your subscription will be activated automatically after confirmation (1-10 minutes)\n"
                                  "🔍 To check payment status: /check_payment",
        'pay_now_button': "💳 Pay Now",
        'qr_code_caption': "Scan the QR code below to copy the payment address:  {pay_address} ",
        'no_pending_payment': "No pending payment to check.",
        'payment_details_not_found': "Pending payment details not found.",
        'payment_expired': "⏳ This payment has expired (more than 20 minutes).\nPlease choose a subscription again.",
        'payment_successful': "✅🥳🤩 Payment confirmed successfully! Your subscription is now active. \n Order ID: {order_id},\n Duration: {duration} Month,\n Channel Link: {channel_link}.\n===========\n (✅🥳🤩تم تأكيد الدفع بنجاح! تم تفعيل الاشتراك.\n معرف الطلب: {order_id},\n المدة: {duration} شهر,\n رابط القناة: {channel_link}.)",
        'payment_failed_cancelled': "❌ Payment failed or cancelled. Please try again.\n======\n (فشل أو إلغاء الدفع. يرجى المحاولة مرة أخرى.)",
        'payment_pending': "⏳ Your payment is still pending. Payment ID: {payment_id}\nPlease complete the payment via the payment address below:\n{pay_address}\n\nWe will notify you once the payment is confirmed.",
        'already_have_pending_payment': "⚠️ You already have an active pending payment. Order ID: {order_id}\nPlease complete the payment via the payment address below:\n{pay_address}",   
        'help_message': "Welcome to OWL CAB Subscriptions Bot! Here are the commands you can use:\n\n"
                        "/start - To start interacting with the bot.\n"
                        "/subscribe - To subscribe to the OWL CAB service.\n"
                        "/check_payment - To check the status of your last payment.\n"
                        "/help - To display this help message.\n",
        'choose_language': "Please choose your preferred language:",
        'arabic_button': "🇸🇦 العربية",
        'english_button': "🇬🇧 English",
        'language_set_to': "Language set to English.",
        'one_day_trial': "1 day - Free Trial",
        'one_month_subscription': "1 month - 1 Month Subscription",
        'three_month_subscription': "3 months - 3 Month Subscription",
        'six_month_subscription': "6 months - 6 Month Subscription",
        'subscribe_command': 'subscribe',
        'check_payment_command': 'check_payment',
        'help_command': 'help',
    }
}
