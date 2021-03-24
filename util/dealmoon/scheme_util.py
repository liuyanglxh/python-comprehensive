MESSAGE_MESSAGE_PAGE = "dealmoon:#message#message#?type=%s&contentId=%d";
DEAL_SHOW = "dealmoon:#deal#show?id=";  # 0
WEB_OPEN = "dealmoon:#web#open?url=";  # 1
EXTERNAL_OPEN = "dealmoon:#external#open?url=";  # 2
MOONSHOW_POST_SHOW = "dealmoon:#moonshow#post#show?id=";  # 4
# ##
# tag聚合页 - 5
# #
MOON_SHOW_TAG = "dealmoon:#moonshow#tag?text=";
# ##
# 品牌聚合页 - 58
# #
MOON_SHOW_BRAND_TAG = "dealmoon:#moonshow#tag?type=brand&id=";
# ##
# 话题聚合页 - 58
# #
MOON_SHOW_TOPIC_TAG = "dealmoon:#moonshow#tag?type=topic&id=";
# ##
# 商家聚合页 - 60
# #
MOON_SHOW_AFFILIATE_TAG = "dealmoon:#moonshow#tag?type=affiliate&id=";

MOONSHOW_TOPIC = "dealmoon:#moonshow#topic?id=";  # 9
LOCAL_SHOW = "dealmoon:#local#show?id=";  # 12
LOCAL_MAIN = "dealmoon:#local#main";  # 13
DEALS_CATEGORY = "dealmoon:#deals#category?id=";  # 15
REDEEM_SHOW = "dealmoon:#redeem#show?id=";  # 19 积分商城
REDEEM_OPEN = "dealmoon:#redeem#open?url=";  # 21 积分商城
GUIDE_MAIN = "dealmoon:#guide#main";  # 23 攻略首页
GUIDE_SHOW = "dealmoon:#guide#show?id=";  # 24 攻略详情
MOONSHOW_GUIDE = "dealmoon:#moonshow#guide#";  # 25 banner跳转到详情
REDEEM_HOME = "dealmoon:#redeem#home";  # 26 积分商城首页
GUIDE_CATEGORY = "dealmoon:#guide#category?id=";  # 28-攻略分类页
COMMENT_VIEW = "dealmoon:#comment#show";  # 30-评论详情
OPEN_INTERNAL_WEB = "dealmoon:#internalweb#open?url=";  # 32-打开内部网页
SCHEME_PRODUCT_REVIEWS = "dealmoon:#productreviews#open?url=";  # 33-众测
SCHEME_PRODUCT_REVIEWS_DETAIL = "dealmoon:#productreviews#open?id=";  # 34-众测详情
DISCLOSURE_DETAIL = "dealmoon:#baoliao#show?id=";  # 40-爆料详情
DISCLOSURE_INDEX = "dealmoon:#baoliao#main";  # 41-爆料首页
DISCLOSURE_USER = "dealmoon:#user#baoliao?id=";  # 42-我的爆料
LOCAL_BUSINESS = "dealmoon:#local#business#show?id=";  # 43-Local商家详情页
LOCAL_DISH = "dealmoon:#dish#detail?id=";  # 53-loca商家推荐菜详情页
SP_SHOW = "dealmoon:#product#show?id=";  # 48-单品
LOCAL_EVENT = "dealmoon:#local#event?id=";  # local活动详情
RANKING_LIST = "dealmoon:#charts#main";  # 排行榜
SP_AREA = "dealmoon:#product#home";  # 单品专区
SP_HOT_AREA = "dealmoon:#product#hot";  # 单品专区最热 scheme
SP_AREA_SUBJECT_DETAILS = "dealmoon:#product#event#show?id=";  # 单品专区专题详情
USER_VOURHER_DETAIL = "dealmoon:#user#voucher?id=";  # 我的代金券详情
VOURHER_DETAIL = "dealmoon:#local#voucher?id=";  # 代金券详情
HAITAO_HOME_SCHEME = "dealmoon:#haitao#home";
CAREFULLY_CHOSEN_SP_SCHEME = "dealmoon:#product#cate#?ids=";
GROUP_BUY_DETAIL = "dealmoon:#internalweb#open?url=";
GROUP_BUY_ACTIVITY_REVIEWS_SCHEME = "dealmoon:#internalweb#open?url=";
HOT_COMMENT_SCHEME = "dealmoon:#hotcomments#show";  # 热评榜scheme
CLICK_RANK_DEAL = "dealmoon:#charts#deal";  # 折扣排行榜
CLICK_RANK_SP = "dealmoon:#charts#product";  # 单品排行榜
CLICK_RANK_TRENDING = "dealmoon:#charts#trending";  # 折扣飙升榜
CLICK_RANK_SP_TRENDING = "dealmoon:#product#trending";  # 单品飙升榜

USER_INVITED_TASK_SCHEME = "dealmoon:#user#invited#task";  # 新人任务页

schemes = [
	DEAL_SHOW,  # 0
	WEB_OPEN,  # 1
	EXTERNAL_OPEN,  # 2
	"dealmoon:#moonshow/main",  # 3
	MOONSHOW_POST_SHOW,  # 4
	MOON_SHOW_TAG,  # 5
	"dealmoon:#user/show?id=",  # 6
	"dealmoon:#moonshow/latestpost",  # 7
	"dealmoon:#moonshow/recommendedpost",  # 8
	MOONSHOW_TOPIC,  # 9
	"dealmoon:#moonshow/hotactivities",  # 10
	"dealmoon:#moonshow/hottags",  # 11
	LOCAL_SHOW,  # 12
	LOCAL_MAIN,  # 13
	"dealmoon:#deals/store?id=",  # 14
	DEALS_CATEGORY,  # 15
	"dealmoon:#message/subscription",  # 16
	"dealmoon:#message/message",  # 17
	"dealmoon:#message/activity",  # 18
	REDEEM_SHOW,  # 19
	"dealmoon:#user/followers",  # 20
	REDEEM_OPEN,  # 21 积分商城
	"dealmoon:#signin/",  # 22 登录
	GUIDE_MAIN,  # 23 攻略首页
	GUIDE_SHOW,  # 24 攻略详情
	MOONSHOW_GUIDE,  # 25 banner跳转到详情
	REDEEM_HOME,  # 26 积分商城首页
	"dealmoon:#user/main",  # 27 跳转到 用户主页  右下角 "我"菜单
	GUIDE_CATEGORY,  # 28 攻略分类页
	"dealmoon:#user/articles",  # 29 ugc个人中心
	COMMENT_VIEW,  # 30 评论详情页
	"dealmoon:#guide/main?source_id=",  # 31 攻略首页并置顶
	"dealmoon:#internalweb/open?url=",  # 32 APP内置浏览器打开wap页面
	SCHEME_PRODUCT_REVIEWS,  # 33 app打开众测页面
	SCHEME_PRODUCT_REVIEWS_DETAIL,  # 34 app打开众测页面
	"dealmoon:#local/feed/new",  # 35 Local最新列表
	"dealmoon:#local/feed/activity",  # 36 Local活动列表
	"dealmoon:#local/feed/guide",  # 37 Local攻略列表
	"dealmoon:#local/feed/scene?id=",  # 38 Local场景列表
	"dealmoon:#local/feed/category?id=",  # 39 Local分类列表
	DISCLOSURE_DETAIL,  # 40爆料详情页
	DISCLOSURE_INDEX,  # 41爆料首页
	DISCLOSURE_USER,  # 42我的爆料
	LOCAL_BUSINESS,  # 43-Local商家详情页
	LOCAL_EVENT,  # 44local活动详情页
	SP_SHOW,  # 45
	RANKING_LIST,  # 46排行榜
	SP_AREA,  # 47单品专区
	SP_AREA_SUBJECT_DETAILS,  # 48单品专区专题详情
	HAITAO_HOME_SCHEME,  # 49 海淘专区
	CAREFULLY_CHOSEN_SP_SCHEME,  # 50 精选好货全部单品
	GROUP_BUY_DETAIL,  # 51 拼团详细页
	GROUP_BUY_ACTIVITY_REVIEWS_SCHEME,  # 52
	LOCAL_DISH,  # 53 商家推荐菜详情
	SP_HOT_AREA,  # 54 单品专区最热
	"dealmoon:#moonshow/compose/post/edit?id=",  # 55 晒货编辑
	HOT_COMMENT_SCHEME,  # 热评榜scheme
	# 57 单品聚合
	"dealmoon:#product/aggregate/",
	# 58
	MOON_SHOW_BRAND_TAG,
	# 59
	MOON_SHOW_TOPIC_TAG,
	# 60
	MOON_SHOW_AFFILIATE_TAG,
	# 61 折扣排行榜
	CLICK_RANK_DEAL,
	# 62 单品排行榜
	CLICK_RANK_SP,
	# 63 折扣飙升榜
	CLICK_RANK_TRENDING,
	# 64 单品飙升榜
	CLICK_RANK_SP_TRENDING
]
