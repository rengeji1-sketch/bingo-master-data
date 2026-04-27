#　電脳八州の検非違使：ビンゴシステム設定ファイル
VERSION = "1.0.1"

 # config.py の中身のイメージ（Colabでまず書いてみる）

 # モード切替
# --- システム基本設定 ---
GAME_MODE = "LAST_SPURT"  # "REALTIME"（即時反映） または "LAST_SPURT"（最後に一括）
TEAM_COUNT = 2          # 参加チーム数
BOARD_SIZE = 5          # 5x5のビンゴ
# 
# 素材データベース
# ID: {名前, タイプ}
ITEMS = {
    1: {"name": "錆びた真鍮ネジ", "type": "basic"},
    2: {"name": "六角の和釘", "type": "basic"},
    3: {"name": "絶縁ボルト", "type": "basic"},
    4: {"name": "蝶型ナット", "type": "basic"},
    5: {"name": "隠しリベット", "type": "basic"},
    6: {"name": "強化ワッシャー", "type": "basic"},
    7: {"name": "超小型歯車（マイクロギア）", "type": "basic"},
    8: {"name": "ゴム製のベルト", "type": "basic"},
    9: {"name": "木製歯車（試作型）", "type": "basic"},
    10: {"name": "磁気ベアリング", "type": "basic"},
    11: {"name": "ピストンクランク", "type": "basic"},
    12: {"name": "タイミングチェーン", "type": "basic"},
    13: {"name": "銅のより線", "type": "basic"},
    14: {"name": "光ファイバーの束", "type": "basic"},
    15: {"name": "抵抗器（レジスタ）", "type": "basic"},
    16: {"name": "コンデンサ", "type": "basic"},
    17: {"name": "放熱板（ヒートシンク）", "type": "basic"},
    18: {"name": "空のデータチップ", "type": "basic"},
    19: {"name": "基盤柄の千代紙", "type": "basic"},
    20: {"name": "竹製光ファイバー", "type": "basic"},
    21: {"name": "朱色の導電ペイント", "type": "basic"},
    22: {"name": "静電気を帯びた水引", "type": "basic"},
    23: {"name": "勾玉のコネクタ", "type": "basic"},
    24: {"name": "電脳提灯の芯", "type": "basic"},
    25: {"name": "強化ガラスの破片", "type": "basic"},
    26: {"name": "アルミのスプリング", "type": "basic"},
    27: {"name": "チタン製の外装板", "type": "basic"},
    28: {"name": "謎の電子キー", "type": "basic"},
    29: {"name": "ゴムのパッキン", "type": "basic"},
    30: {"name": "変換アダプタ", "type": "basic"},
    # ...提案した素材をここに並べる
}

# 3枚成立素材
TRIO_RECIPES = {
    101: {"name": "三連同調歯車", "ITEMS": [7, 9, 10]},  # 超小型歯車 + 木製歯車 + 磁気ベアリング
    102: {"name": "強化クランク軸", "ITEMS":[11, 6, 2]}, #ピストンクランク×強化ワッシャー×六角の和釘
    103: {"name": "高回転プーリー", "ITEMS":[8, 26, 12]}, #ゴム製の伝達ベルト×アルミのスプリング×タイミングチェーン
    104: {"name": "油圧式伸縮脚", "ITEMS":[11, 29, 27]}, #ピストンクランク×ゴムのパッキン×チタン製の外装板
    105: {"name": "振動抑制ダンパー", "ITEMS":[29, 26, 6]}, #ゴムのパッキン×アルミのスプリング×強化ワッシャー
    106: {"name": "八州式論理基板", "ITEMS":[18, 15, 16]}, #空のデータチップ×抵抗器×コンデンサ
    107: {"name": "冷却ファンユニット", "ITEMS":[17, 7, 3]}, #放熱板×超小型歯車×絶縁ボルト
    108: {"name": "信号変換機", "ITEMS":[30, 13, 14]}, #変換アダプタ×銅のより線×光ファイバーの束
    109: {"name": "高耐圧コンデンサ陣", "ITEMS":[16, 16, 3]}, #コンデンサ×コンデンサ×絶縁ボルト
    110: {"name": "電脳墨汁回路", "ITEMS":[21, 19, 15]}, #朱色の導電ペイント×基盤の千代紙×抵抗器
    111: {"name": "電脳提灯ランプ", "ITEMS":[24, 25, 13]}, #電脳提灯の芯×強化ガラスの破片×銅のより線
    112: {"name": "竹型アンテナモジュール", "ITEMS":[20, 13, 30]}, #竹製光ファイバー×銅のより線×変換アダプタ
    113: {"name": "三稜鏡（プリズム）センサ", "ITEMS":[25, 25, 23]}, #強化ガラスの破片×強化ガラスの破片×勾玉のコネクタ
    114: {"name": "光通信ケーブル束", "ITEMS":[14, 14, 23]}, #光ファイバーの束×光ファイバーの束×静電気を帯びた水引
    115: {"name": "偽装ホログラム発生器", "ITEMS":[18, 25, 17]}, #空のデータチップ×強化ガラスの破片×放熱板
    116: {"name": "複合強化装甲パネル", "ITEMS":[27, 26, 5]}, #チタン製の外装版×アルミのスプリング×隠しリベット
    117: {"name": "電脳水引結束バンド", "ITEMS":[22, 22, 23]}, #静電気を帯びた水引×静電気を帯びた水引×勾玉のコネクタ
    118: {"name": "耐衝撃フレーム", "ITEMS":[27, 6, 4]}, #チタン製の外装版×強化ワッシャー×蝶型ナット
    119: {"name": "絶縁ジョイント", "ITEMS":[3, 4, 29]}, #絶縁ボルト×蝶型ナット×ゴムのパッキン
    120: {"name": "隠密固定用リベット", "ITEMS":[5, 5, 21]}, #隠しリベット×隠しリベット×朱色の導電ペイント
    121: {"name": "検非違使の認証鍵", "ITEMS":[28, 18, 23]}, #謎の電子キー×空のデータチップ×勾玉のコネクタ
    122: {"name": "九十九（つくも）の動力源", "ITEMS":[1, 9, 22]}, #錆びた真鍮ネジ×木製歯車×静電気を帯びた水引
    123: {"name": "電脳千代紙シールド", "ITEMS":[19, 19, 21]}, #基盤柄の千代紙×基盤柄の千代紙×朱色の導電ペイント
    124: {"name": "再生ジャンクユニット", "ITEMS":[1, 13, 26]}, #錆びた真鍮ネジ×銅のより線×アルミのスプリング
    125: {"name": "変換式勾玉コネクタ", "ITEMS":[23, 30, 14]}, #勾玉のコネクタ×変換アダプタ×光ファイバーの束

    # ...IDの組み合わせで定義する
}
# レシピがないと作れない素材
CRAFT_RECIPES = {
    201: {"name": "八州式・電磁防壁", "materials": [116, 21], "recipe_id": 501, "magic_circle": {"image_file": "mc_circle_cyan.png", "color": "cyan", "text": "防壁", "style": "pixel"}}, #複合強化装甲パネル×朱色の導電ペイント
    202: {"name": "雷鳴の機巧刀","materials": [27, 22, 14], "recipe_id": 502, "magic_circle": {"shape": "triangle", "color": "yellow", "text": "雷鳴", "style": "kanji"}}, #チタン製の外装版×静電気を帯びた水引×光ファイバーの束
    203: {"name": "重力制御リアクター", "materials": [11, 11, 26], "recipe_id": 503, "magic_circle": {"shape": "square", "color": "purple", "text": "重力", "style": "glitch"}}, #磁気ベアリング×三連同調歯車×謎の電子キー
    204: {"name": "電脳勾玉の結界", "materials": [23, 23, 19], "recipe_id": 504, "magic_circle": {"shape": "hexagon", "color": "green", "text": "結界", "style": "ancient"}},
    205: {"name": "八州巡回ドローン", "materials": [12, 17, 18], "recipe_id": 505, "magic_circle": {"shape": "cross", "color": "orange", "text": "巡回", "style": "pixel"}},
    206: {"name": "耐火防護装甲", "materials": [27, 29, 15], "recipe_id": 506, "magic_circle": {"shape": "octagon", "color": "red", "text": "耐火", "style": "bold"}},
    207: {"name": "超高密度コンデンサ", "materials": [16, 16, 16], "recipe_id": 507, "magic_circle": {"shape": "circle", "color": "blue", "text": "蓄電", "style": "glitch"}},
    208: {"name": "量子通信アンテナ", "materials": [14, 20, 30], "recipe_id": 508, "magic_circle": {"shape": "star", "color": "lime", "text": "通信", "style": "pixel"}},
    209: {"name": "電脳墨汁ジェット", "materials": [21, 21, 13], "recipe_id": 509, "magic_circle": {"shape": "rhombus", "color": "black", "text": "墨汁", "style": "kanji"}},
    210: {"name": "光学迷彩スーツ", "materials": [25, 25, 18], "recipe_id": 510, "magic_circle": {"shape": "circle", "color": "white", "text": "隠形", "style": "ancient"}},
    211: {"name": "全天候型センサー", "materials": [25, 17, 30], "recipe_id": 511, "magic_circle": {"shape": "square", "color": "pink", "text": "探知", "style": "pixel"}},
    212: {"name": "八州伝統紋様回路", "materials": [19, 21, 22], "recipe_id": 512, "magic_circle": {"shape": "hexagon", "color": "gold", "text": "伝統", "style": "kanji"}},
    213: {"name": "超伝導水引ケーブル", "materials": [22, 13, 23], "recipe_id": 513, "magic_circle": {"shape": "triangle", "color": "silver", "text": "伝導", "style": "bold"}},
    214: {"name": "自動修復リベット", "materials": [5, 5, 26], "recipe_id": 514, "magic_circle": {"shape": "circle", "color": "brown", "text": "修復", "style": "glitch"}},
    215: {"name": "電脳提灯・極", "materials": [24, 24, 16], "recipe_id": 515, "magic_circle": {"shape": "octagon", "color": "yellow", "text": "極光", "style": "ancient"}},
    216: {"name": "多重ジョイント・アーム", "materials": [11, 4, 3], "recipe_id": 516, "magic_circle": {"shape": "square", "color": "grey", "text": "多軸", "style": "pixel"}},
    217: {"name": "空間歪曲レンズ", "materials": [25, 23, 14], "recipe_id": 517, "magic_circle": {"shape": "circle", "color": "violet", "text": "歪曲", "style": "glitch"}},
    218: {"name": "朱色回路の認証キー", "materials": [28, 21, 19], "recipe_id": 518, "magic_circle": {"shape": "hexagon", "color": "crimson", "text": "認証", "style": "kanji"}},
    219: {"name": "防塵密閉パッキン", "materials": [29, 29, 6], "recipe_id": 519, "magic_circle": {"shape": "octagon", "color": "navy", "text": "密閉", "style": "bold"}},
    220: {"name": "検非違使・最終認証基板", "materials": [18, 28, 23], "recipe_id": 520,"magic_circle": {"shape": "star", "color": "teal", "text": "最終", "style": "ancient"}},

}
# 素材ではなく「設計図」。これを読み込むと対応する高度素材が作れるようになる。
RECIPE_CARDS = {
    501:{"name": "電磁防壁の設計図","target_id": 201},
    502: {"name": "機巧刀の鍛錬書", "target_id": 202},
    503: {"name": "重力アームの仕様書","target_id": 203},
    504: {"name": "勾玉結界の符", "target_id": 204},
    505: {"name": "巡回ドローンの配置図", "target_id": 205},
    506: {"name": "防護装甲の製法", "target_id": 206},
    507: {"name": "高密度回路の技術書", "target_id": 207},
    508: {"name": "通信アンテナの設計図", "target_id": 208},
    509: {"name": "墨汁回路の調合書", "target_id": 209},
    510: {"name": "迷彩スーツの型紙", "target_id": 210},
    511: {"name": "センサー技術仕様書", "target_id": 211},
    512: {"name": "紋様回路の写し", "target_id": 212},
    513: {"name": "超伝導ケーブルの仕様書", "target_id": 213},
    514: {"name": "自動修復リベットの設計図", "target_id": 214},
    515: {"name": "電脳提灯・極の構造図", "target_id": 215},
    516: {"name": "多重ジョイントの図面", "target_id": 216},
    517: {"name": "歪曲レンズの加工書", "target_id": 217},
    518: {"name": "朱色回路の解読キー", "target_id": 218},
    519: {"name": "密閉パッキンの設計図", "target_id": 219},
    520: {"name": "最終認証基板の設計図", "target_id": 220},

}
# 自分のビンゴを助ける特殊なカード。
WILD_CARDS = {
    301: {"name": "八州の万能ネジ", "effect": "substitute_any", "target": "self", "count": 1, "log_msg": "【複製】{user}は盤面の回路をコピーし、新たなマスを埋めた！", "color": "GOLD"}, #好きなマスの素材1つ分として代用できる。
    302: {"name": "写し鏡の回路", "effect": "copy_slot", "target": "self", "copy_limit": 1, "log_msg": "【解析】{user}の智慧が光る！レシピなしで強引に合成を成功させた！", "color": "GOLD"}, #すでに自分の盤面で埋まっているマスを一つ選び、その中身をコピーして別の空きマスに貼り付ける
    303: {"name": "即席レシピ「智慧の輪」", "effect": "force_complete", "target": "self", "uses": 1, "log_msg": "【解析】{user}の智慧が光る！レシピなしで強引に合成を成功させた！", "color": "GOLD"}, #「レシピが必要になる素材」を、レシピを持っていない状態で一回だけ強引に合成できる
    304: {"name": "電脳水引の結び直し", "effect": "patch_trio", "target": "self", "required_min": 1, "log_msg": "【修復】{user}が水引を結び直す！足りない素材を補填しTRIOを完成させた！", "color": "GOLD"}, #「三枚成立カード」のうち、すでに１～２枚埋まっているマスの不足分を、手持ちの「基本素材」何でも一つで補充して完成させる
    305: {"name": "神風のショートカット", "effect": "instant_bingo_slot", "target": "self", "reach_only": True, "log_msg": "【大逆転】神風が吹いた！{user}のリーチ箇所が奇跡的に埋まる！", "color": "CYAN"}, #ビンゴのリーチがかかっているとき、最後の一マスを「素材なし」で即座に埋める
    306: {"name": "リサイクル・ジャック", "effect": "recycle_material", "target": "self", "refund_rate": 1.0, "log_msg": "【回収】{user}は回路を分解し、使用済みの素材をデータに還元した！", "color": "GOLD"}, #一度埋めたマスを一つ空け、そこに使っていた素材を全て手元（データ）に戻す　構成ミスを直すときに便利
    307: {"name": "五行の加護（シールド）", "effect": "shield_active", "target": "self", "hp": 1, "log_msg": "【防壁】五行の力が宿る！{user}の盤面に鉄壁のシールドが展開された！", "color": "GOLD"}, #自分の盤面の任意の一マスをロックする　後述の「お邪魔カード」による破壊を一回だけ防ぐ
    308: {"name": "検非違使の特権", "effect": "system_gift", "target": "self", "logic": "smart_fill", "log_msg": "【特権】システム介入！{user}へ今最も必要な素材が特別に付与された！", "color": "GOLD"}, #大画面のビンゴ全体を見て、今一番必要としている素材をシステムが一つ選んで付与してくれる
    309: {"name": "二重起動（ツイン・ブースト）", "effect": "double_count", "target": "self", "multiplier": 2, "log_msg": "【加速】ツイン・ブースト！{user}の次の読み取りは2倍の出力となる！", "color": "CYAN"}, #次に読み込む素材QRを「２倍」としてカウントする（三枚成立なら一気に二マス分埋まる）
    310: {"name": "大盤振る舞いの宝船", "effect": "line_unlock", "target": "self", "line_count": 1, "log_msg": "【祝福】宝船が入港！{user}が指定したラインのレシピ制限が解除された！", "color": "GOLD"}, #自分のビンゴの「縦・横・斜め」のどこか１ラインを指定し、そのライン上の全ての「レシピが必要な素材」の条件を解除する
}
# 相手を邪魔したり、盤面を操作したりするカード。
HACK_CARDS = {
    401: {"name": "ノイズ・ハッキング", "effect": "blind_enemy", "target": "enemy", "duration": 60, "log_msg": "【妨害】{user}からの攻撃！{target}の画面がノイズで塗りつぶされる！", "color": "RED"}, #敵チームの画面に1分間デジタルノイズを走らせ、ビンゴの状況を隠して見えなくする
    402: {"name": "錆びつきの呪い", "effect": "reset_slot", "target": "enemy", "reset_count": 1, "log_msg": "【侵食】{user}が呪いを送信！{target}の素材が錆びつき、マスが空いてしまった！", "color": "RED"}, #敵チームの「基本素材」で埋まったマスを１つ選び、未完了（空きマス）に戻してしまう
    403: {"name": "回路の短絡（ショート）", "effect": "break_trio", "target": "enemy", "break_limit": 1, "log_msg": "【破壊】ショート発生！{target}の三枚成立回路がバラバラに破壊された！", "color": "RED"}, #敵チームの「三枚成立カード」の進歩をリセットし、揃っていた素材をバラバラにする
    404: {"name": "検非違使の検問", "effect": "scan_jamming", "target": "enemy", "block_count": 1, "log_msg": "【検問】{user}が検問を設置！{target}の次のスキャンは無効化される！", "color": "RED"}, #敵チームが次にQRを読み取った際、「偽物」と判定して素材を受け付けなくさせる（１回使い切り）
    405: {"name": "重力の歪み", "effect": "rotate_board", "target": "enemy", "angle": 90, "log_msg": "【重力】空間が歪む！{target}の盤面が強制的に90度回転させられた！", "color": "PURPLE"}, #敵チームのビンゴ盤面を９０度回転させる。狙っていたラインがズレて戦略を練り直させる
    406: {"name": "素材の霧散", "effect": "delete_stock", "target": "enemy", "delete_count": 2, "log_msg": "【消失】{user}がウイルスを注入！{target}の手持ちデータが霧のように消えた！", "color": "RED"}, #敵チームが今持っている「未登録の素材データ」をランダムに２つ消去する。
    407: {"name": "レシピの文字化け", "effect": "disable_recipe", "target": "enemy", "duration": 180, "log_msg": "【混乱】{target}のレシピデータが文字化け！一定時間、高度合成が不能になる！", "color": "PURPLE"}, #敵チームが持っているレシピを１つ選び、３分間使えなくする
    408: {"name": "電脳八州の夜", "effect": "light_off", "target": "enemy", "duration": 30, "log_msg": "【静寂】{user}が夜を呼ぶ。{target}の視界が奪われ、周囲が闇に包まれた！", "color": "NAVY"}, #３０秒間、敵チームの読み取り端末のライトを強制オフにし、暗い場所での探索を困難にする
    409: {"name": "座標の書き換え", "effect": "swap_coordinates", "target": "enemy", "swap_count": 1, "log_msg": "【移報】空間入れ替え！{user}と{target}の盤面データが一部交換された！", "color": "PURPLE"}, #自分の盤面の「何も埋まっていないマス」と、敵の「すでに埋まっているマス」の位置を入れ替える
    410: {"name": "強制シャッフル", "effect": "shuffle_board", "target": "enemy", "intensity": "high", "log_msg": "【混沌】カオス・ハック！{target}の全素材がランダムにシャッフルされた！", "color": "PURPLE"}, #敵チームのビンゴ盤面にある素材を全てランダムに並べ替える　ビンゴ直前のチームへの致命的な一撃
}

SHIKIGAMI_LIST = {
    601: {"name": "熱鎮（ネツチン）", "element": "火", "personality": "冷静沈黙（※過熱時：暴言モード）", "craft": "京仏具（凝縮・彫金）", "skills": ["冷却回路（クールダウン・リンク）", "熱量制御（ヒート・コントロール）"],
        "description": "暴走する熱を仏具の彫金技術で美しい「形」に封じ込める。普段は静かだが、限界を超えると口が悪くなる。"},
    602: {
        "name": "土成（ドセイ）",
        "element": "地",
        "personality": "チャラい自信家（※中身：超一流の職人魂）",
        "craft": "清水焼（成形・焼成）",
        "skills": ["基盤安定化（ベース・スタビライズ）", "構造修復（ストラクチャー・リペア）"],
        "description": "崩壊する地面を瞬時に美しい陶器の床へと焼き固める。ノリは軽いが、仕事の精度には絶対の妥協を許さない。"
    },
    603: {
        "name": "瞬電（シュンデン）",
        "element": "雷",
        "personality": "だらだら省エネ（※本性：天才ハッカー）",
        "craft": "西陣織（緻密な回路紋様）",
        "skills": ["電力最適化（パワー・オプティマイズ）", "スパーク制御（スパーク・コントロール）"],
        "description": "西陣織のような複雑な電子回路を編み上げる。いつもは面倒くさがっているが、キーボードを叩く速さは光速。"
    },
    604: {
        "name": "水清（スイセイ）",
        "element": "水",
        "personality": "のんびり屋（※実は：冷徹な監査官）",
        "craft": "京友禅（色彩美・浄化）",
        "skills": ["情報浄化（データ・クレンズ）", "フロー制御（フロー・コントロール）"],
        "description": "京友禅の染めの技で汚れたデータを元の美しさへ戻す。のんびりしているが、不正データには一切の容赦がない。"
    },
    605: {
        "name": "風導（フウドウ）",
        "element": "風",
        "personality": "博学多才（※実は：武闘派）",
        "craft": "京扇子（風の方向性）",
        "skills": ["情報伝播（インフォメーション・ブリーズ）", "経路最適化（パス・オプティマイズ）"],
        "description": "扇子を用いて情報の流れを自在に操る。知的な物知りだが、いざとなると扇子を武器に最前線で暴れる。"
    },
    606: {
        "name": "照輝（ショウキ）",
        "element": "光",
        "personality": "ストイック（※実は：甘党）",
        "craft": "京硝子・京切子（屈折・可視化）",
        "skills": ["情報可視化（データ・イルミネーション）", "光の回線（ライトニング・リンク）"],
        "description": "光を屈折させ、隠された情報を暴き出す。常に自分に厳しい求道者だが、和菓子を見ると目が輝いてしまう。"
    },
    607: {
        "name": "闇封（アンフウ）",
        "element": "闇",
        "personality": "お祭り騒ぎ（※実は：寂しがり屋）",
        "craft": "京漆器（封印・漆の艶）",
        "skills": ["影の潜行（シャドウ・ハック）", "情報隔離（データ・アイソレーション）"],
        "description": "漆を塗り重ねるように情報を隔離し、封印する。賑やかで騒がしいが、誰からも連絡がないと途端に落ち込む。"
    },
    608: {
        "name": "氷断（ヒョウダン）",
        "element": "氷",
        "personality": "礼儀正しい騎士（※実は：毒舌家）",
        "craft": "京打刃物（鋭利な切断）",
        "skills": ["感情解凍（エモーション・デフラグ）", "思考促進（シンキング・アクセラレート）"],
        "description": "不要な思考を鋭い刃で切り捨て、整理する。態度は非常に丁寧だが、笑顔で心に刺さる毒を吐くことがある。"
    },
    609: {
        "name": "結樹（ユウキ）",
        "element": "木",
        "personality": "明るい太陽（※実は：支配欲が強い）",
        "craft": "京くみひも（結合・結び）",
        "skills": ["情報剪定（データ・プルーニング）", "循環促進（サイクル・ブースト）"],
        "description": "「結び」の力でデータ同士を強固に繋ぐ。明るく前向きだが、一度結んだものは二度と離さない独占欲を持つ。"
    },
    610: {
        "name": "幻筆（ゲンピツ）",
        "element": "幻",
        "personality": "ミステリアス（※実は：運動音痴）",
        "craft": "京筆（記述・境界）",
        "skills": ["現実境界（リアリティ・バリア）", "幻影解除（イリュージョン・ブレイク）"],
        "description": "京筆で空中に描いたものを現実に変える。神秘的な雰囲気を纏っているが、何もないところでよく転ぶ。"
    }
}
print("設定ファイルの読み込みテスト完了。素材数:", len(ITEMS))
print(len(TRIO_RECIPES))

# --- あなたの「手持ちアイテム」リスト（ここを書き換えて遊べます） ---
# パターンA：材料もレシピも揃っている状態
my_items = [27, 22, 14, 502, 1, 5]

# --- 判定プログラム（ここが bingo_logic.py の心臓部になります） ---
def check_craftable(target_id, inventory):
    recipe = CRAFT_RECIPES[target_id]

    # 1. レシピを持っているかチェック
    if recipe["recipe_id"] not in inventory:
        return False, "レシピが足りません"

    # 2. 材料がすべて揃っているかチェック
    for m_id in recipe["materials"]:
        if m_id not in inventory:
            return False, f"材料ID {m_id} が足りません"

    return True, "合成可能です！魔法陣起動！"

# --- 実行！ ---
can_make, message = check_craftable(202, my_items)
print(f"【判定結果】: {message}")
