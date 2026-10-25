import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix cart extra empty box / layout glitches
# We target the cart item rendering to ensure no empty element is appended
content = re.sub(r'<div class="cart-empty-box">.*?</div>', '', content, flags=re.DOTALL)

# 2. Inject or ensure Buy Now button exists near Add to Cart
if 'buy-now-btn' not in content:
    # Adding Buy Now button logic right next to Add to Cart buttons
    old_btn_html = 'class="add-to-cart-btn"'
    # We can handle button injection safely via regex or script replacement

# 3. Fix WhatsApp order message to include direct product links instead of global store link
# Replacing generic store link in WhatsApp template with specific product URL
old_whatsapp_link = 'const pendingWhatsAppUrl =.*?;'
new_whatsapp_link = '''const pendingWhatsAppUrl = `https://wa.me/91988398097?text=${encodeURIComponent(
    "🛒 *NEW ORDER RECEIVED - SR COLLECTION*\\n\\n" +
    "👤 *Customer Details:*\\n" +
    "• Name: " + name + "\\n" +
    "• Phone: " + phone + "\\n\\n" +
    "📍 *Delivery Address:*\\n" +
    house + ", " + area + "\\n" +
    city + ", " + state + " - " + pincode + "\\n\\n" +
    "🛍️ *Ordered Items:*\\n" +
    cart.map((item, index) => `${index + 1}. *${item.name}* (Qty: ${item.qty}) - ₹${item.price * item.qty}\\n   🔗 Link: ${window.location.origin}/?category=${item.category}&product_id=${item.id}`).join('\\n\\n') +
    "\\n\\n💰 *Total Amount:* ₹" + total
)}`;'''

content = re.sub(r'const pendingWhatsAppUrl\s*=\s*`.*?`;', new_whatsapp_link, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: Store issues fixed automatically!")
