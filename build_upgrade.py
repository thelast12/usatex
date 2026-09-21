from pathlib import Path
import json, re, shutil, zipfile

ROOT=Path('/mnt/data/seo_pro_work')
BASE=ROOT/'index.html'
BASE_TEXT=BASE.read_text(encoding='utf-8')

pages={
'index.html':{
 'path':'/', 'tab':'salary',
 'title':'Salary Tax Calculator 2026 — Take-Home Pay | TaxCalc USA',
 'desc':'Free 2026 U.S. salary and paycheck calculator. Estimate federal income tax, state tax, Social Security, Medicare, and take-home pay for all 50 states.',
 'keywords':'salary tax calculator 2026, paycheck calculator, take home pay calculator, payroll tax calculator, federal tax calculator, state tax calculator, net pay calculator',
 'h1':'U.S. Salary & Paycheck<br><em>Tax Calculator</em>',
 'hero':'Estimate your 2026 take-home pay from salary, hourly, or monthly income with federal, state, and payroll tax calculations.',
 'eyebrow':'FREE 2026 PAYCHECK CALCULATOR',
 'h2':'Calculate your take-home pay',
 'intro':'Enter your income, filing status, state, pay frequency, and deductions to see an estimated paycheck breakdown. Use the result to understand how gross pay turns into net pay.',
 'bullets':['Federal income tax estimate','State income tax and payroll deductions','Social Security and Medicare estimates','Annual, monthly, and paycheck views'],
 'faqs':[
 ('How does the salary tax calculator work?','Enter your income and filing details, then calculate to see an estimated breakdown of taxes and take-home pay.'),
 ('Can I use it for hourly income?','Yes. The salary calculator includes an hourly income mode so you can estimate annualized pay and take-home pay.'),
 ('Does the calculator cover all states?','The calculator includes state selections for all 50 U.S. states and is designed for 2026 estimates.'),
 ],
},
'overtime/index.html':{
 'path':'/overtime/', 'tab':'overtime',
 'title':'Overtime Pay Tax Calculator 2026 — OT Take-Home Pay | TaxCalc USA',
 'desc':'Calculate 2026 overtime pay, gross earnings, estimated taxes, and take-home pay. Compare regular and overtime hours with a free U.S. overtime calculator.',
 'keywords':'overtime calculator 2026, overtime pay calculator, overtime tax calculator, time and a half calculator, OT paycheck calculator',
 'h1':'Overtime Pay<br><em>Tax Calculator</em>',
 'hero':'Estimate regular pay, overtime earnings, gross income, and taxes when you work extra hours.',
 'eyebrow':'2026 OVERTIME PAY CALCULATOR',
 'h2':'Calculate overtime earnings and take-home pay',
 'intro':'Enter your base hourly rate, regular hours, overtime hours, and overtime multiplier. The calculator shows how additional hours affect gross pay and estimated taxes.',
 'bullets':['Regular and overtime hours','1.5× and other overtime multipliers','Annualized gross earnings','Estimated federal and payroll taxes'],
 'faqs':[
 ('How is overtime pay calculated?','The calculator starts with your hourly base rate, regular hours, overtime hours, and selected overtime multiplier to estimate gross overtime earnings.'),
 ('Can I use a multiplier other than 1.5×?','Yes. The overtime calculator lets you choose from the available overtime rate options in the calculator.'),
 ('Does overtime get taxed differently?','Overtime earnings are generally part of your taxable wages. Your actual withholding depends on your overall payroll and tax situation.'),
 ],
},
'self-employed/index.html':{
 'path':'/self-employed/', 'tab':'selfemployed',
 'title':'Self-Employment Tax Calculator 2026 — SE Tax | TaxCalc USA',
 'desc':'Estimate 2026 self-employment tax, federal income tax, and take-home income for freelancers, contractors, and business owners with a free calculator.',
 'keywords':'self employment tax calculator 2026, freelance tax calculator, 1099 tax calculator, contractor tax calculator, SE tax calculator',
 'h1':'Self-Employment<br><em>Tax Calculator</em>',
 'hero':'Estimate self-employment tax and after-tax income from freelance, contractor, and independent-business earnings.',
 'eyebrow':'2026 SELF-EMPLOYMENT TAX CALCULATOR',
 'h2':'Estimate taxes on self-employed income',
 'intro':'Use your business income and deductible expenses to estimate self-employment tax and federal tax. This is useful for freelancers, independent contractors, and other 1099 earners.',
 'bullets':['Business income and expenses','Self-employment tax estimate','Federal income tax estimate','After-tax income planning'],
 'faqs':[
 ('Who can use the self-employment calculator?','It is designed for freelancers, independent contractors, sole proprietors, and other people receiving self-employed income.'),
 ('Can I include business expenses?','Yes. Enter eligible business expenses in the calculator to estimate taxable business income.'),
 ('Is this a tax filing tool?','No. It is an estimation and planning calculator, not a substitute for filing a tax return or professional tax advice.'),
 ],
},
'tax-refund/index.html':{
 'path':'/tax-refund/', 'tab':'refund',
 'title':'Tax Refund Estimator 2026 — Estimate Your Federal Refund | TaxCalc USA',
 'desc':'Estimate your 2026 federal tax refund or balance due using income, filing status, deductions, credits, and withholding information.',
 'keywords':'tax refund calculator 2026, refund estimator, federal tax refund calculator, tax refund estimate, refund calculator USA',
 'h1':'2026 Tax Refund<br><em>Estimator</em>',
 'hero':'Estimate whether you may receive a federal tax refund or have a balance due based on income, deductions, credits, and withholding.',
 'eyebrow':'FREE 2026 TAX REFUND ESTIMATOR',
 'h2':'Estimate your federal tax refund',
 'intro':'Enter the income, tax withheld, deductions, and credits requested by the estimator. The result provides a planning estimate of your refund or amount due.',
 'bullets':['Federal income tax estimate','Tax withholding comparison','Deductions and credits inputs','Refund or balance-due estimate'],
 'faqs':[
 ('What does a tax refund estimate show?','It compares an estimated federal tax liability with the amount of tax already withheld and applicable credits to estimate a refund or balance due.'),
 ('Why can my actual refund be different?','Your filed return can include additional income, deductions, credits, withholding, or tax rules that differ from the assumptions used in an estimate.'),
 ('Can I use this before filing?','Yes. Refund estimates are useful for planning before you prepare or file a federal return.'),
 ],
},
'state-compare/index.html':{
 'path':'/state-compare/', 'tab':'compare',
 'title':'State Income Tax Comparison 2026 — Compare All 50 States | TaxCalc USA',
 'desc':'Compare U.S. state income tax treatment for 2026. Explore state tax differences and estimated take-home pay with a free comparison calculator.',
 'keywords':'state income tax comparison 2026, state tax calculator, compare state taxes, income tax by state, state paycheck calculator',
 'h1':'State Income Tax<br><em>Comparison 2026</em>',
 'hero':'Compare estimated state income tax and take-home pay across U.S. states using a consistent calculator setup.',
 'eyebrow':'2026 STATE TAX COMPARISON',
 'h2':'Compare income taxes by state',
 'intro':'Select a salary and filing setup, then compare estimated state-tax effects. Use the comparison as a starting point when evaluating take-home pay in different states.',
 'bullets':['All 50 U.S. states','State income tax estimates','Comparable salary scenarios','Take-home pay comparisons'],
 'faqs':[
 ('Can I compare all 50 states?','Yes. The comparison tool includes state selections covering all 50 U.S. states.'),
 ('Are state taxes the only difference between states?','No. Local taxes, deductions, credits, payroll taxes, and other rules can also affect a person’s final tax outcome.'),
 ('Is the comparison an exact tax quote?','No. It is an estimate based on the inputs and assumptions in the calculator.'),
 ],
},
'converter/index.html':{
 'path':'/converter/', 'tab':'convert',
 'title':'Salary to Hourly Converter 2026 — Hourly Rate Calculator | TaxCalc USA',
 'desc':'Convert annual salary to hourly, monthly, weekly, and paycheck rates for 2026. Reverse-calculate salary from an hourly wage with a free converter.',
 'keywords':'salary to hourly calculator 2026, hourly rate calculator, annual salary to hourly, hourly to salary calculator, paycheck converter',
 'h1':'Salary to Hourly<br><em>Converter</em>',
 'hero':'Convert annual salary and hourly wages into equivalent hourly, weekly, monthly, and yearly pay amounts.',
 'eyebrow':'2026 SALARY & HOURLY CONVERTER',
 'h2':'Convert salary to hourly pay',
 'intro':'Choose the direction of the conversion, enter your pay amount, and set your work schedule. The converter helps compare compensation across salary and hourly formats.',
 'bullets':['Annual ↔ hourly conversion','Monthly and weekly equivalents','Hours-per-week inputs','Simple compensation comparisons'],
 'faqs':[
 ('How do I convert salary to an hourly rate?','Enter your annual salary and work schedule. The converter uses those inputs to estimate an equivalent hourly rate.'),
 ('Can I convert hourly pay to salary?','Yes. Use the hourly mode to estimate an annualized salary from an hourly wage and work schedule.'),
 ('Does the converter calculate taxes?','The converter focuses on gross-pay conversions. Use the Salary Tax Calculator for an estimated after-tax paycheck.'),
 ],
},
'bonus-tax/index.html':{
 'path':'/bonus-tax/', 'tab':'bonus',
 'title':'Bonus Tax Calculator 2026 — Bonus Take-Home Pay | TaxCalc USA',
 'desc':'Estimate taxes and take-home pay on a 2026 bonus. Compare bonus gross pay, federal withholding, payroll taxes, and estimated net bonus.',
 'keywords':'bonus tax calculator 2026, bonus paycheck calculator, bonus withholding calculator, supplemental wages tax calculator, bonus take home pay',
 'h1':'Bonus Tax<br><em>Calculator 2026</em>',
 'hero':'Estimate how federal and payroll tax withholding can affect the take-home amount of a bonus.',
 'eyebrow':'2026 BONUS TAX CALCULATOR',
 'h2':'Estimate your bonus take-home pay',
 'intro':'Enter your bonus amount and relevant payroll information to estimate withholding and net bonus pay. Use the result for planning before your bonus is paid.',
 'bullets':['Gross bonus amount','Estimated federal withholding','Social Security and Medicare','Estimated net bonus'],
 'faqs':[
 ('Why can my bonus paycheck look heavily taxed?','Bonus withholding can make the amount withheld from a single payment look different from your normal paycheck. Final tax liability is determined on your tax return.'),
 ('Is bonus withholding the same as final tax?','No. Payroll withholding is a prepayment toward your tax liability; your final liability depends on your full-year tax situation.'),
 ('Can I use this for a one-time bonus?','Yes. The calculator is designed for estimating the tax effect of a bonus payment.'),
 ],
},
'w4-helper/index.html':{
 'path':'/w4-helper/', 'tab':'w4',
 'title':'W-4 Withholding Calculator & Helper 2026 — TaxCalc USA',
 'desc':'Use this 2026 W-4 withholding helper to estimate paycheck withholding and understand how filing status, income, and adjustments affect federal withholding.',
 'keywords':'W-4 calculator 2026, W4 withholding calculator, W-4 helper, paycheck withholding estimator, federal withholding calculator',
 'h1':'W-4 Withholding<br><em>Calculator & Helper</em>',
 'hero':'Estimate federal paycheck withholding and understand the information used when completing a Form W-4.',
 'eyebrow':'2026 W-4 WITHHOLDING HELPER',
 'h2':'Estimate paycheck withholding',
 'intro':'Use the helper to explore how filing status, income, and adjustments can affect estimated federal withholding. Always use the official IRS Form W-4 instructions when completing the form.',
 'bullets':['Filing status inputs','Income and adjustment inputs','Estimated federal withholding','Links to official IRS resources'],
 'faqs':[
 ('Does this replace the IRS W-4?','No. It is a planning helper. The official IRS form and instructions should be used when you actually complete Form W-4.'),
 ('Can withholding be different from final tax?','Yes. Withholding is an amount paid through payroll during the year. Your final federal tax liability is determined when you file your return.'),
 ('Can I use this after changing jobs?','Yes. It can help you explore withholding scenarios when your income or filing situation changes.'),
 ],
},
'401k-ira/index.html':{
 'path':'/401k-ira/', 'tab':'retirement',
 'title':'401(k) & IRA Calculator 2026 — Retirement Contribution Planner | TaxCalc USA',
 'desc':'Estimate 2026 401(k) and IRA contributions, retirement savings growth, and tax-aware take-home effects with a free planning calculator.',
 'keywords':'401k calculator 2026, IRA calculator 2026, retirement calculator, 401k contribution calculator, Roth IRA calculator, retirement savings calculator',
 'h1':'401(k) & IRA<br><em>Retirement Calculator</em>',
 'hero':'Explore 401(k) and IRA contribution scenarios and see how retirement savings can affect your long-term plan and paycheck.',
 'eyebrow':'2026 RETIREMENT CONTRIBUTION CALCULATOR',
 'h2':'Plan 401(k) and IRA contributions',
 'intro':'Compare retirement contribution scenarios using your income, contribution amounts, and account type. Use the results to understand contribution levels and projected savings.',
 'bullets':['401(k) contribution planning','Traditional vs. Roth IRA scenarios','Contribution and savings estimates','Paycheck impact planning'],
 'faqs':[
 ('What can the retirement calculator estimate?','It can help you explore contribution amounts, account types, and projected retirement savings using the inputs you provide.'),
 ('What is the difference between traditional and Roth contributions?','Traditional and Roth accounts can have different tax treatment. The calculator lets you explore the available account scenarios rather than providing individualized tax advice.'),
 ('Should I treat the result as financial advice?','No. It is a planning calculator. Contribution decisions should consider your complete financial situation and applicable plan rules.'),
 ],
},
}

# CSS additions
style_marker='</style>\n\n<script type="application/ld+json">'
css=r'''
/* ─── SEO CONTENT / ACCESSIBILITY UPGRADE ─── */
.seo-intro-wrap{max-width:1400px;margin:0 auto;padding:0 20px 8px}
.seo-intro{background:linear-gradient(135deg,rgba(0,212,255,.055),rgba(123,47,255,.045));border:1px solid var(--border2);border-radius:16px;padding:22px 24px;margin:8px 0 20px}
.seo-intro .seo-eyebrow{font-size:.68rem;letter-spacing:.12em;font-weight:800;color:var(--cyan);margin-bottom:7px}
.seo-intro h2{margin:0 0 8px;font-size:1.15rem;color:var(--text)}
.seo-intro p{margin:0;color:var(--text2);font-size:.88rem;line-height:1.75;max-width:1000px}
.seo-points{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin-top:16px}
.seo-point{padding:11px 12px;border:1px solid var(--border);border-radius:10px;background:var(--card);color:var(--text2);font-size:.76rem;line-height:1.45}
.seo-faq{max-width:1400px;margin:0 auto;padding:0 20px 26px}
.seo-faq h2{font-size:1.08rem;margin:0 0 12px;color:var(--text)}
.seo-faq-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.seo-faq details{border:1px solid var(--border);background:var(--card);border-radius:10px;padding:12px 14px}
.seo-faq summary{cursor:pointer;font-weight:700;font-size:.8rem;color:var(--text);line-height:1.45}
.seo-faq details p{margin:9px 0 0;color:var(--text2);font-size:.76rem;line-height:1.65}
.seo-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.seo-links a{display:inline-flex;align-items:center;padding:7px 10px;border-radius:8px;border:1px solid var(--border);background:var(--card);color:var(--cyan);text-decoration:none;font-size:.74rem;font-weight:700}
.seo-links a:hover{background:var(--card2);border-color:var(--border2)}
@media(max-width:900px){.seo-points{grid-template-columns:1fr 1fr}.seo-faq-grid{grid-template-columns:1fr}}
@media(max-width:520px){.seo-intro-wrap,.seo-faq{padding-left:12px;padding-right:12px}.seo-intro{padding:17px}.seo-points{grid-template-columns:1fr}}
'''

paths={v['tab']:v['path'] for v in pages.values()}
labels={'salary':'Salary Tax Calculator','overtime':'Overtime Pay','selfemployed':'Self-Employment Tax','refund':'Tax Refund Estimator','compare':'State Tax Comparison','convert':'Salary to Hourly Converter','bonus':'Bonus Tax Calculator','w4':'W-4 Withholding Helper','retirement':'401(k) & IRA Calculator'}

def schema_for(meta):
    url='https://usataxes.online'+meta['path']
    crumbs=[{'@type':'ListItem','position':1,'name':'TaxCalc USA','item':'https://usataxes.online/'}]
    if meta['path']!='/':
        crumbs.append({'@type':'ListItem','position':2,'name':labels[meta['tab']],'item':url})
    return [
      {'@context':'https://schema.org','@type':'WebSite','name':'TaxCalc USA','url':'https://usataxes.online/','inLanguage':'en-US'},
      {'@context':'https://schema.org','@type':'WebApplication','name':meta['title'].split(' — ')[0],'url':url,'description':meta['desc'],'applicationCategory':'FinanceApplication','operatingSystem':'Any','offers':{'@type':'Offer','price':'0','priceCurrency':'USD'},'isAccessibleForFree':True,'inLanguage':'en-US'},
      {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':crumbs}
    ]

def ld_script(obj):
    return '<script type="application/ld+json">\n'+json.dumps(obj,ensure_ascii=False,indent=2)+'\n</script>'

def seo_block(meta):
    pts=''.join(f'<div class="seo-point">✓ {p}</div>' for p in meta['bullets'])
    faq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in meta['faqs'])
    links=[]
    # 4 contextual links, excluding current
    for tab,path in list(paths.items()):
        if tab==meta['tab']: continue
        links.append(f'<a href="{path}" onclick="event.preventDefault();showTab(\'{tab}\')">{labels[tab]}</a>')
        if len(links)>=4: break
    return f'''\n<section class="seo-intro-wrap" aria-labelledby="seo-page-heading">\n  <div class="seo-intro">\n    <div class="seo-eyebrow">{meta['eyebrow']}</div>\n    <h2 id="seo-page-heading">{meta['h2']}</h2>\n    <p>{meta['intro']}</p>\n    <div class="seo-points">{pts}</div>\n    <div class="seo-links" aria-label="Related calculators">{''.join(links)}</div>\n  </div>\n</section>\n<section class="seo-faq" aria-labelledby="faq-heading">\n  <h2 id="faq-heading">Common questions</h2>\n  <div class="seo-faq-grid">{faq}</div>\n</section>\n'''

for rel,meta in pages.items():
    s=BASE_TEXT
    # Remove old FAQ schema entirely (Google removed FAQ rich-result docs in 2026)
    s=re.sub(r'<script type="application/ld\+json">\s*\{\s*"@context": "https://schema\.org",\s*"@type": "FAQPage".*?</script>\s*', '', s, flags=re.S)
    # Replace all existing JSON-LD blocks with clean page-specific schema
    s=re.sub(r'<script type="application/ld\+json">.*?</script>\s*', '', s, flags=re.S)
    # Head metadata
    s=re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', s, count=1, flags=re.S)
    s=re.sub(r'<meta name="description"[^>]*>', f'<meta name="description" content="{meta["desc"]}">', s, count=1)
    s=re.sub(r'<meta name="keywords"[^>]*>', f'<meta name="keywords" content="{meta["keywords"]}">', s, count=1)
    s=re.sub(r'<link rel="canonical"[^>]*>', f'<link rel="canonical" href="https://usataxes.online{meta["path"]}">', s, count=1)
    s=re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="https://usataxes.online{meta["path"]}">', s, count=1)
    s=re.sub(r'<meta property="og:title"[^>]*>', f'<meta property="og:title" content="{meta["title"]}">', s, count=1)
    s=re.sub(r'<meta property="og:description"[^>]*>', f'<meta property="og:description" content="{meta["desc"]}">', s, count=1)
    s=re.sub(r'<meta name="twitter:title"[^>]*>', f'<meta name="twitter:title" content="{meta["title"]}">', s, count=1)
    s=re.sub(r'<meta name="twitter:description"[^>]*>', f'<meta name="twitter:description" content="{meta["desc"]}">', s, count=1)
    # Ensure strong robots/theme/referrer metadata
    if '<meta name="theme-color"' not in s:
        s=s.replace('<meta name="robots"', '<meta name="theme-color" content="#0a0f1e">\n<meta name="referrer" content="strict-origin-when-cross-origin">\n<meta name="robots"',1)
    # Correct PWA icon path
    s=s.replace('href="/usatex/favicon.svg"','href="/favicon.svg"')
    # Add schemas before </head>
    schemas='\n'.join(ld_script(x) for x in schema_for(meta))
    s=s.replace('</head>', schemas+'\n</head>',1)
    # CSS
    if 'SEO CONTENT / ACCESSIBILITY UPGRADE' not in s:
        s=s.replace('</style>\n\n</head>',css+'\n</style>\n\n</head>',1)
        # In case the exact marker differs
        if 'SEO CONTENT / ACCESSIBILITY UPGRADE' not in s:
            s=s.replace('</style>\n\n<script',css+'\n</style>\n\n<script',1)
    # Hero h1 and copy
    s=re.sub(r'<h1>.*?</h1>', f'<h1>{meta["h1"]}</h1>', s, count=1, flags=re.S)
    # Replace hero first paragraph after h1 only
    s=re.sub(r'(<h1>.*?</h1>\s*<p>).*?(</p>)', lambda m:m.group(1)+meta['hero']+m.group(2), s, count=1, flags=re.S)
    # Make nav crawlable anchors; JS still controls SPA navigation
    navmap=[('salary','/','Salary'),('overtime','/overtime/','Overtime'),('selfemployed','/self-employed/','Self-Employed'),('refund','/tax-refund/','Refund Est.'),('compare','/state-compare/','State Compare'),('convert','/converter/','Converter'),('bonus','/bonus-tax/','Bonus Tax'),('w4','/w4-helper/','W-4 Helper'),('retirement','/401k-ira/','401k / IRA')]
    old_patterns=[r'<button class="nav-btn active" onclick="showTab\(\'salary\'\)">Salary</button>']
    # Replace all nav buttons in main nav generically
    def repl_nav(m):
        body=m.group(1)
        for tab,path,label in navmap:
            body=body.replace(f'<button class="nav-btn active" onclick="showTab(\'{tab}\')">{label}</button>',f'<a class="nav-btn'+(' active' if tab==meta['tab'] else '')+f'" href="{path}" onclick="event.preventDefault();showTab(\'{tab}\')">{label}</a>')
            body=body.replace(f'<button class="nav-btn" onclick="showTab(\'{tab}\')">{label}</button>',f'<a class="nav-btn'+(' active' if tab==meta['tab'] else '')+f'" href="{path}" onclick="event.preventDefault();showTab(\'{tab}\')">{label}</a>')
        return '<nav id="mainNav">'+body+'</nav>'
    s=re.sub(r'<nav id="mainNav">(.*?)</nav>',repl_nav,s,count=1,flags=re.S)
    # Mobile nav buttons -> crawlable anchors
    for tab,path,label in navmap:
        patterns=[
            (f'<button class="mobile-nav-btn active" onclick="showTab(\'{tab}\');closeMobileNav()">',f'<a class="mobile-nav-btn'+(' active' if tab==meta['tab'] else '')+f'" href="{path}" onclick="event.preventDefault();closeMobileNav();showTab(\'{tab}\')">'),
            (f'<button class="mobile-nav-btn" onclick="closeMobileNav();showTab(\'{tab}\')">',f'<a class="mobile-nav-btn'+(' active' if tab==meta['tab'] else '')+f'" href="{path}" onclick="event.preventDefault();closeMobileNav();showTab(\'{tab}\')">')
        ]
        for a,b in patterns:s=s.replace(a,b)
        s=s.replace(f'</button>',f'</a>') if False else s
    # Fix only mobile nav button closing tags within drawer
    start=s.find('<div id="mobileNavDrawer"')
    end=s.find('</div>',start)
    # easier regex over class
    s=re.sub(r'(<a class="mobile-nav-btn[^>]*>[^<]*?)</button>',r'\1</a>',s)
    # Insert SEO block before tabs (after hero section close and before TABS comment)
    if '<section class="seo-intro-wrap"' not in s:
        idx=s.find('<!-- TABS -->')
        s=s[:idx]+seo_block(meta)+'\n'+s[idx:]
    # Initial visible page should match URL even before load JS: set target page block display:block and all others none is already inline only salary default.
    # Change the target page's opening style and hide salary if target != salary; JS still normalizes on load.
    if meta['tab']!='salary':
        s=s.replace('<div id="page-salary">','<div id="page-salary" style="display:none">',1)
        target_id='page-'+meta['tab']
        s=s.replace(f'<div id="{target_id}" style="display:none">',f'<div id="{target_id}">',1)
    # Remove the in-page SEO file download helper/button because production already ships sitemap/robots/manifest.
    s=re.sub(r'\s*<p style="margin-top:10px"><button onclick="generateSEOFiles\(\)".*?</button></p>', '', s, flags=re.S)
    # Replace internal generator URLs with custom-domain URLs if function remains (harmless but clean)
    s=s.replace('https://thelast12.github.io/usatex/', 'https://usataxes.online/')
    s=s.replace("'/usatex/", "'/")
    s=s.replace('"/usatex/', '"/')
    s=s.replace("'/usatex'", "'/'")
    # Keep only root-relative path mapping, no project prefix in service worker fallback
    (ROOT/rel).parent.mkdir(parents=True,exist_ok=True)
    (ROOT/rel).write_text(s,encoding='utf-8')

# Production support files
robots='''User-agent: *\nAllow: /\n\nSitemap: https://usataxes.online/sitemap.xml\n'''
(ROOT/'robots.txt').write_text(robots,encoding='utf-8')

urls=[v['path'] for v in pages.values()]
sitemap='''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''+''.join(f'  <url><loc>https://usataxes.online{u}</loc></url>\n' for u in urls)+'''</urlset>\n'''
(ROOT/'sitemap.xml').write_text(sitemap,encoding='utf-8')

manifest={
 'name':'TaxCalc USA — U.S. Tax Calculators',
 'short_name':'TaxCalc USA',
 'description':'Free U.S. salary, payroll, overtime, self-employment, refund, W-4 and retirement calculators.',
 'start_url':'/', 'scope':'/', 'display':'standalone', 'background_color':'#0a0f1e','theme_color':'#0a0f1e','lang':'en-US','orientation':'portrait-primary',
 'icons':[{'src':'/favicon.svg','sizes':'any','type':'image/svg+xml','purpose':'any maskable'}]
}
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')

sw='''const CACHE_NAME = 'taxcalc-usa-v3';\nconst APP_SHELL = [\n  '/', '/overtime/', '/self-employed/', '/tax-refund/', '/state-compare/',\n  '/converter/', '/bonus-tax/', '/w4-helper/', '/401k-ira/', '/manifest.json', '/favicon.svg'\n];\nself.addEventListener('install', event => {\n  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(APP_SHELL)).then(() => self.skipWaiting()));\n});\nself.addEventListener('activate', event => {\n  event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))).then(() => self.clients.claim()));\n});\nself.addEventListener('fetch', event => {\n  if (event.request.method !== 'GET') return;\n  event.respondWith(caches.match(event.request).then(cached => cached || fetch(event.request).then(response => {\n    const copy = response.clone();\n    if (response.ok && new URL(event.request.url).origin === self.location.origin) {\n      caches.open(CACHE_NAME).then(cache => cache.put(event.request, copy));\n    }\n    return response;\n  }).catch(() => caches.match('/'))));\n});\n'''
(ROOT/'sw.js').write_text(sw,encoding='utf-8')

readme='''TaxCalc USA — SEO PRO production build\n\nIncludes:\n- 9 crawlable calculator URLs on https://usataxes.online/\n- Unique title, meta description, H1, intro and FAQ content per calculator\n- Crawlable navigation links with SPA behavior preserved\n- Canonical, Open Graph, Twitter metadata and page-specific Breadcrumb/WebApplication/WebSite JSON-LD\n- Clean robots.txt and sitemap.xml\n- PWA manifest and multi-route service worker\n- Existing calculator JavaScript and UI preserved from the working stable build\n\nUpload/replace these files in the repository:\nindex.html\novertime/index.html\nself-employed/index.html\ntax-refund/index.html\nstate-compare/index.html\nconverter/index.html\nbonus-tax/index.html\nw4-helper/index.html\n401k-ira/index.html\nrobots.txt\nsitemap.xml\nmanifest.json\nsw.js\n\nKeep your existing CNAME, ads.txt and favicon.svg if they are already in the repo.\n'''
(ROOT/'README.txt').write_text(readme,encoding='utf-8')

# Basic validations
for rel,meta in pages.items():
    s=(ROOT/rel).read_text(encoding='utf-8')
    assert f'<title>{meta["title"]}</title>' in s
    assert f'canonical" href="https://usataxes.online{meta["path"]}"' in s
    assert '<script type="application/ld+json">' in s
    assert 'FAQPage' not in s
    assert '<section class="seo-intro-wrap"' in s
    assert f'<h1>{meta["h1"]}</h1>' in s
    assert f'href="{meta["path"]}"' in s
print('Built',len(pages),'pages')
