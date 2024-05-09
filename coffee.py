from bs4 import BeautifulSoup
import json

html_code = '''<div
  class="m6QErb DxyBCb kA9KIf dS8AEf ecceSd"
  aria-label="Results for government office kktc"
  role="feed"
  tabindex="-1"
>
  <div class="m6QErb z7i0C">
    <div
      class="fp2VUc"
      aria-roledescription="carousel"
      aria-label="Available filters for this search"
      role="region"
      jsaction="keydown:pane.wfvdle3699.navigate; mousedown:pane.wfvdle3699.dragCards; mousewheel:pane.wfvdle3699.navigate wheel:pane.wfvdle3699.navigate; DOMMouseScroll:pane.wfvdle3699.navigate; focus:pane.wfvdle3699.focus; mousemove:pane.wfvdle3699.focus"
      jslog="127728;"
    >
      <div jslog="127734; track:click;"></div>
      <div class="rHNip cRLbXd" style="min-height: 0px">
        <div class="GXRbod" style="width: 4px"></div>
        <div class="dryRY">
          <div class="KNfEk siaXSd ODcthf">
            <button
              class="e2moi"
              aria-haspopup="menu"
              aria-label="Rating"
              jsaction="pane.wfvdle3700;keydown:ripple.play;mousedown:ripple.play;ptrdown:ripple.play"
              jslog="8292; track:click;"
            >
              <div class="tXNTee L6Bbsd VbYL9">
                <div class="OyjIsf"></div>
                <span class="uEubGf fontTitleSmall">Rating</span
                ><span class="drGLxe google-symbols" aria-hidden="true"></span>
              </div>
            </button>
          </div>
          <div class="KNfEk siaXSd ODcthf">
            <button
              class="e2moi"
              aria-haspopup="dialog"
              aria-label="Hours"
              jsaction="pane.wfvdle3701;keydown:ripple.play;mousedown:ripple.play;ptrdown:ripple.play"
              jslog="8402; track:click;"
            >
              <div class="tXNTee L6Bbsd VbYL9">
                <div class="OyjIsf"></div>
                <span class="uEubGf fontTitleSmall">Hours</span
                ><span class="drGLxe google-symbols" aria-hidden="true"></span>
              </div>
            </button>
          </div>
          <div class="ODcthf">
            <button
              class="e2moi"
              aria-label="All filters"
              jsaction="pane.wfvdle3702;keydown:ripple.play;mousedown:ripple.play;ptrdown:ripple.play"
              jslog="37790; track:click;"
            >
              <div class="tXNTee L6Bbsd VbYL9">
                <div class="OyjIsf"></div>
                <span class="k48Abe google-symbols" aria-hidden="true"></span
                ><span class="uEubGf fontTitleSmall">All filters</span>
              </div>
            </button>
          </div>
        </div>
        <div class="GXRbod" style="width: 0px"></div>
      </div>
      <div jslog="127730; track:click;"></div>
      <div class="TSAyb"></div>
    </div>
  </div>
  <div class="JrN27d SuV3fd Zjt37e TGiyyc">
    <div class="MFHMle y2jPs"></div>
    <div class="Ntshyc">
      <div class="L1xEbb">
        <h1 class="fontTitleLarge IFMGgb">Results</h1>
        <div class="whqM4e">
          <div
            jslog="151371; track:click;"
            class="iwhWtc x9tric"
            data-callout-id="ucc-35"
          >
            <div class="PSwX3c"></div>
            <div class="zXYuJe Rot3te">
              <span class="VfPpkd-suEOdc-sM5MNb-OWXEXe-nzrxxc"
                ><div
                  class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"
                  data-is-touch-wrapper="true"
                >
                  <button
                    class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-INsAgc VfPpkd-LgbsSe-OWXEXe-icon-M1Soyc VfPpkd-LgbsSe-OWXEXe-dgl2Hf Rj2Mlf OLiIxf PDpWxe LQeN7 s73B3c MyHLpd wphPJc Q8G3mf"
                    jscontroller="soHxf"
                    jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc; touchcancel:JMtRjd; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;mlnRJb:fLiPzd"
                    data-idom-class="Rj2Mlf OLiIxf PDpWxe LQeN7 s73B3c MyHLpd wphPJc Q8G3mf"
                    aria-label="Learn more about legal disclosure regarding public reviews on Google Maps"
                    data-tooltip-enabled="true"
                    data-tooltip-is-rich="true"
                    data-tooltip-is-persistent="true"
                    data-tooltip-id="ucc-35"
                    data-tooltip-with-caret="true"
                    data-tooltip-with-caret-position="11"
                  >
                    <div class="VfPpkd-Jh9lGc"></div>
                    <div class="VfPpkd-J1Ukfc-LhBDec"></div>
                    <div class="VfPpkd-RLmnJb"></div>
                    <span class="VfPpkd-kBDsod" aria-hidden="true"
                      ><img
                        class="qy5xwd"
                        src="https://www.gstatic.com/images/icons/material/system_gm/2x/info_gm_grey_18dp.png"
                        alt="" /></span
                    ><span jsname="V67aGc" class="VfPpkd-vQzf8d"></span>
                  </button>
                </div>
                <div
                  jsshadow=""
                  jsaction="BfpAHf:TCTP9d;Nwyqre:DsZxZc; transitionend:e204de"
                  jscontroller="HmEm0"
                  data-title-id-disregard="ucc-36"
                  id="ucc-35"
                  class="VfPpkd-suEOdc VfPpkd-suEOdc-OWXEXe-nzrxxc ziykHb TA5ace d1Bfob undefined"
                  role="status"
                  data-mdc-tooltip-persistent="true"
                  tabindex="-1"
                  data-mdc-tooltip-has-caret="true"
                >
                  <div class="VfPpkd-z59Tgd-OiiCO">
                    <div class="VfPpkd-z59Tgd" aria-hidden="true">
                      <span
                        aria-hidden="true"
                        class="VfPpkd-BFbNVe-bF1uUb NZp2ef"
                      ></span>
                      <div jsslot="" class="VfPpkd-IqDDtd">
                        <div class="mF2nKf">
                          <div class="hWnRWc">About these results</div>
                          <br />
                          <div class="EFUAFd">
                            When you search for businesses or places near a
                            location, Google Maps will show you local results.
                            Several factors - primarily relevance, distance, and
                            prominence - are combined to help find the best
                            results for your search.
                          </div>
                          <div class="EFUAFd">
                            <a
                              href="https://support.google.com/maps/answer/3092445?entry=ttu&amp;utm_source=maps&amp;authuser=0&amp;hl=en"
                              >Learn more</a
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="VfPpkd-Djsh7e-XxIAqe-ma6Yeb">
                      <span
                        aria-hidden="true"
                        class="VfPpkd-BFbNVe-bF1uUb NZp2ef"
                      ></span>
                    </div>
                    <div class="VfPpkd-Djsh7e-XxIAqe-bottom">
                      <span
                        aria-hidden="true"
                        class="VfPpkd-BFbNVe-bF1uUb NZp2ef"
                      ></span>
                    </div>
                  </div></div
              ></span>
            </div>
          </div>
        </div>
      </div>
      <div class="wuvLZe fontBodyMedium"></div>
    </div>
    <div class="MFHMle"><div class="kiXRrd"></div></div>
  </div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3703;mouseout:pane.wfvdle3703"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Posta Dairesi"
        href="https://www.google.com/maps/place/KKTC+Posta+Dairesi/data=!4m7!3m6!1s0x14de17004eab06d1:0x42e02b18a2df209b!8m2!3d35.17845!4d33.3599633!16s%2Fg%2F11y448k2ny!19sChIJ0QarTgAX3hQRmyDfohgr4EI?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3703;focus:pane.wfvdle3703;blur:pane.wfvdle3703;auxclick:pane.wfvdle3703;keydown:pane.wfvdle3703;clickmod:pane.wfvdle3703"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJQlNnQSIsbnVsbCwxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Posta Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59H5+9XG</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3706;keydown:pane.wfvdle3706;mouseover:pane.wfvdle3706;mouseout:pane.wfvdle3706"
                aria-label="Get directions to KKTC Posta Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3707;mouseout:pane.wfvdle3707"
    >
      <a
        class="hfpxzc"
        aria-label="Grenzübergang"
        href="https://www.google.com/maps/place/Grenz%C3%BCbergang/data=!4m7!3m6!1s0x14de170009bd3985:0xc89ee90c3596cadb!8m2!3d35.1771797!4d33.3548199!16s%2Fg%2F11vz0qq6t3!19sChIJhTm9CQAX3hQR28qWNQzpnsg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3707;focus:pane.wfvdle3707;blur:pane.wfvdle3707;auxclick:pane.wfvdle3707;keydown:pane.wfvdle3707;clickmod:pane.wfvdle3707"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJRmlnQSIsbnVsbCwyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Grenzübergang</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59G3+VWG Ave. 21, Markou Drakou</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3709;keydown:pane.wfvdle3709;mouseover:pane.wfvdle3709;mouseout:pane.wfvdle3709"
                aria-label="Get directions to Grenzübergang"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJRmlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3710;mouseout:pane.wfvdle3710"
    >
      <a
        class="hfpxzc"
        aria-label="Kyrenia District Administration Office"
        href="https://www.google.com/maps/place/Kyrenia+District+Administration+Office/data=!4m7!3m6!1s0x14de17844beb7593:0x7061ac59583bc8cf!8m2!3d35.1665565!4d33.3539811!16s%2Fg%2F11l6vk_hg1!19sChIJk3XrS4QX3hQRz8g7WFmsYXA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3710;focus:pane.wfvdle3710;blur:pane.wfvdle3710;auxclick:pane.wfvdle3710;keydown:pane.wfvdle3710;clickmod:pane.wfvdle3710"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJTENnQSIsbnVsbCwzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kyrenia District Administration Office
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5983+GHV, Dimostheni Severi</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3713;keydown:pane.wfvdle3713;mouseover:pane.wfvdle3713;mouseout:pane.wfvdle3713"
                aria-label="Get directions to Kyrenia District Administration Office"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJTENnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3714;mouseout:pane.wfvdle3714"
    >
      <a
        class="hfpxzc"
        aria-label="κλινική"
        href="https://www.google.com/maps/place/%CE%BA%CE%BB%CE%B9%CE%BD%CE%B9%CE%BA%CE%AE/data=!4m7!3m6!1s0x14de119b5d0fa195:0x74ebeb1ecdc274af!8m2!3d35.1740602!4d33.344958!16s%2Fg%2F11vj54xt7p!19sChIJlaEPXZsR3hQRr3TCzR7r63Q?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3714;focus:pane.wfvdle3714;blur:pane.wfvdle3714;auxclick:pane.wfvdle3714;keydown:pane.wfvdle3714;clickmod:pane.wfvdle3714"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJUXlnQSIsbnVsbCw0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">κλινική</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Filiou Zannetou 25-1100</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3717;keydown:pane.wfvdle3717;mouseover:pane.wfvdle3717;mouseout:pane.wfvdle3717"
                aria-label="Get directions to κλινική"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJUXlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3718;mouseout:pane.wfvdle3718"
    >
      <a
        class="hfpxzc"
        aria-label="Enformasyon Dairesi"
        href="https://www.google.com/maps/place/Enformasyon+Dairesi/data=!4m7!3m6!1s0x14de172d5f7d24d3:0xe8ddb6e6560c4bee!8m2!3d35.195645!4d33.3498019!16s%2Fg%2F11bycm9hmy!19sChIJ0yR9Xy0X3hQR7ksMVua23eg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3718;focus:pane.wfvdle3718;blur:pane.wfvdle3718;auxclick:pane.wfvdle3718;keydown:pane.wfvdle3718;clickmod:pane.wfvdle3718"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJVnlnQSIsbnVsbCw1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Enformasyon Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>58WX+7W3, Selçuklu Cd</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3752;keydown:pane.wfvdle3752;mouseover:pane.wfvdle3752;mouseout:pane.wfvdle3752"
                aria-label="Visit Enformasyon Dairesi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJVnlnQSIsIixBT3ZWYXcwMlplalV1ZWxxbGJnT2tsUWUxSG1GLCwwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E2MWdJWWlnSywiXQ=="
                href="http://pio.mfa.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3720;keydown:pane.wfvdle3720;mouseover:pane.wfvdle3720;mouseout:pane.wfvdle3720"
                aria-label="Get directions to Enformasyon Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJVnlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3721;mouseout:pane.wfvdle3721"
    >
      <a
        class="hfpxzc"
        aria-label="Turkish Republic of Northern Cyprus Ministry of Foreign Affairs"
        href="https://www.google.com/maps/place/Turkish+Republic+of+Northern+Cyprus+Ministry+of+Foreign+Affairs/data=!4m7!3m6!1s0x14de1732a310d86f:0xbd696952a9bb9afd!8m2!3d35.1952122!4d33.3499137!16s%2Fg%2F11b7m9hg9q!19sChIJb9gQozIX3hQR_Zq7qVJpab0?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3721;focus:pane.wfvdle3721;blur:pane.wfvdle3721;auxclick:pane.wfvdle3721;keydown:pane.wfvdle3721;clickmod:pane.wfvdle3721"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJYXlnQSIsbnVsbCw2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Turkish Republic of Northern Cyprus Ministry of Foreign
                      Affairs
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.8 stars 48 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.8</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(48)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>58WX+3XM, Selçuklu Cd</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 32 41</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3723;keydown:pane.wfvdle3723;mouseover:pane.wfvdle3723;mouseout:pane.wfvdle3723"
                aria-label="Visit Turkish Republic of Northern Cyprus Ministry of Foreign Affairs's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJYXlnQSIsIixBT3ZWYXcxZ2Z0NGk3OUVPUWYwUk5uOTAxN3dwLCwwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E2MWdJZkNnUCwiXQ=="
                href="http://mfa.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3724;keydown:pane.wfvdle3724;mouseover:pane.wfvdle3724;mouseout:pane.wfvdle3724"
                aria-label="Get directions to Turkish Republic of Northern Cyprus Ministry of Foreign Affairs"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJYXlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3725;mouseout:pane.wfvdle3725"
    >
      <a
        class="hfpxzc"
        aria-label="Kıbrıs Türk radyo"
        href="https://www.google.com/maps/place/K%C4%B1br%C4%B1s+T%C3%BCrk+radyo/data=!4m7!3m6!1s0x14de17bae8a3ba57:0xc8db77204091e920!8m2!3d35.1873081!4d33.3635033!16s%2Fg%2F11sd_22tsf!19sChIJV7qj6LoX3hQRIOmRQCB328g?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3725;focus:pane.wfvdle3725;blur:pane.wfvdle3725;auxclick:pane.wfvdle3725;keydown:pane.wfvdle3725;clickmod:pane.wfvdle3725"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJa2dFb0FBIixudWxsLDdd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kıbrıs Türk radyo
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Şht. Arif Salih Sk 16</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3727;keydown:pane.wfvdle3727;mouseover:pane.wfvdle3727;mouseout:pane.wfvdle3727"
                aria-label="Get directions to Kıbrıs Türk radyo"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJa2dFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3728;mouseout:pane.wfvdle3728"
    >
      <a
        class="hfpxzc"
        aria-label="Γραφείο Ε.Ο.Τ. Κύπρου"
        href="https://www.google.com/maps/place/%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF+%CE%95.%CE%9F.%CE%A4.+%CE%9A%CF%8D%CF%80%CF%81%CE%BF%CF%85/data=!4m7!3m6!1s0x14de17b347fa0cf5:0x3c4f20b0cc883507!8m2!3d35.1608892!4d33.3693684!16s%2Fg%2F11pzy81z2b!19sChIJ9Qz6R7MX3hQRBzWIzLAgTzw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3728;focus:pane.wfvdle3728;blur:pane.wfvdle3728;auxclick:pane.wfvdle3728;keydown:pane.wfvdle3728;clickmod:pane.wfvdle3728"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJb3dFb0FBIixudWxsLDhd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Γραφείο Ε.Ο.Τ. Κύπρου
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >5969+9P5, Λεωφόρος Αρχιεπισκόπου Μακαρίου Γ</span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3731;keydown:pane.wfvdle3731;mouseover:pane.wfvdle3731;mouseout:pane.wfvdle3731"
                aria-label="Get directions to Γραφείο Ε.Ο.Τ. Κύπρου"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJb3dFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3732;mouseout:pane.wfvdle3732"
    >
      <a
        class="hfpxzc"
        aria-label="TRNC Presidency"
        href="https://www.google.com/maps/place/TRNC+Presidency/data=!4m7!3m6!1s0x14de1747c2984a59:0x666131a74bb769b5!8m2!3d35.1811251!4d33.3606843!16s%2Fg%2F1vhnt_rn!19sChIJWUqYwkcX3hQRtWm3S6cxYWY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3732;focus:pane.wfvdle3732;blur:pane.wfvdle3732;auxclick:pane.wfvdle3732;keydown:pane.wfvdle3732;clickmod:pane.wfvdle3732"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJdUFFb0FBIixudWxsLDld"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">TRNC Presidency</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.3 stars 18 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.3</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(18)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Tanzimat Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 34 44</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3753;keydown:pane.wfvdle3753;mouseover:pane.wfvdle3753;mouseout:pane.wfvdle3753"
                aria-label="Visit TRNC Presidency's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJdUFFb0FBIiwiLEFPdlZhdzNIdFpjRkwxSWQzUDVpdWpoeWZkZC0sLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0l4d0VvRFEsIl0="
                href="http://www.kktcb.org/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3734;keydown:pane.wfvdle3734;mouseover:pane.wfvdle3734;mouseout:pane.wfvdle3734"
                aria-label="Get directions to TRNC Presidency"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJdUFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3735;mouseout:pane.wfvdle3735"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Telekomünikasyon Dairesi"
        href="https://www.google.com/maps/place/KKTC+Telekom%C3%BCnikasyon+Dairesi/data=!4m7!3m6!1s0x14de17397ca5b783:0x2ee0e1ec3b699ade!8m2!3d35.1862941!4d33.3634308!16s%2Fg%2F1tfm3_j2!19sChIJg7elfDkX3hQR3pppO-zh4C4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3735;focus:pane.wfvdle3735;blur:pane.wfvdle3735;auxclick:pane.wfvdle3735;keydown:pane.wfvdle3735;clickmod:pane.wfvdle3735"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMGdFb0FBIixudWxsLDEwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Telekomünikasyon Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.1 stars 25 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.1</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(25)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Şht. Arif Salih Sk 1</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 444 14 44</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3737;keydown:pane.wfvdle3737;mouseover:pane.wfvdle3737;mouseout:pane.wfvdle3737"
                aria-label="Visit KKTC Telekomünikasyon Dairesi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMGdFb0FBIiwiLEFPdlZhdzJQRHRQMzBESG9MelFDZ05pNlJNLXEsLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0k0UUVvRFEsIl0="
                href="http://telekom.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3738;keydown:pane.wfvdle3738;mouseover:pane.wfvdle3738;mouseout:pane.wfvdle3738"
                aria-label="Get directions to KKTC Telekomünikasyon Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMGdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3739;mouseout:pane.wfvdle3739"
    >
      <a
        class="hfpxzc"
        aria-label="TC Lefkoşa Büyükelçiliği Kalkınma ve Ekonomik İşbirliği Ofisi"
        href="https://www.google.com/maps/place/TC+Lefko%C5%9Fa+B%C3%BCy%C3%BCkel%C3%A7ili%C4%9Fi+Kalk%C4%B1nma+ve+Ekonomik+%C4%B0%C5%9Fbirli%C4%9Fi+Ofisi/data=!4m7!3m6!1s0x14de1736bea53801:0xd00d6933c5faacbe!8m2!3d35.1878716!4d33.3553632!16s%2Fg%2F11c529qyqk!19sChIJATilvjYX3hQRvqz6xTNpDdA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3739;focus:pane.wfvdle3739;blur:pane.wfvdle3739;auxclick:pane.wfvdle3739;keydown:pane.wfvdle3739;clickmod:pane.wfvdle3739"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJOWdFb0FBIixudWxsLDExXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      TC Lefkoşa Büyükelçiliği Kalkınma ve Ekonomik İşbirliği
                      Ofisi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 3 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(3)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>No:86 KKTC, Bedrettin Demirel Caddesi</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 610 07 00</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3741;keydown:pane.wfvdle3741;mouseover:pane.wfvdle3741;mouseout:pane.wfvdle3741"
                aria-label="Visit TC Lefkoşa Büyükelçiliği Kalkınma ve Ekonomik İşbirliği Ofisi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJOWdFb0FBIiwiLEFPdlZhdzJObG9IazZwd0xkT2ktckFKNVZBbVQsLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0lod0lvRHcsIl0="
                href="http://www.kei.gov.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3742;keydown:pane.wfvdle3742;mouseover:pane.wfvdle3742;mouseout:pane.wfvdle3742"
                aria-label="Get directions to TC Lefkoşa Büyükelçiliği Kalkınma ve Ekonomik İşbirliği Ofisi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJOWdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3743;mouseout:pane.wfvdle3743"
    >
      <a
        class="hfpxzc"
        aria-label="TRNC Ministry of Tourism"
        href="https://www.google.com/maps/place/TRNC+Ministry+of+Tourism/data=!4m7!3m6!1s0x14de1741386402fb:0x6007e20010a18aed!8m2!3d35.176907!4d33.36617!16s%2Fg%2F1tdhp16k!19sChIJ-wJkOEEX3hQR7YqhEADiB2A?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3743;focus:pane.wfvdle3743;blur:pane.wfvdle3743;auxclick:pane.wfvdle3743;keydown:pane.wfvdle3743;clickmod:pane.wfvdle3743"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJblFJb0FBIixudWxsLDEyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      TRNC Ministry of Tourism
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.7 stars 15 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(15)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Haydarpaşa Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 96 29</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3754;keydown:pane.wfvdle3754;mouseover:pane.wfvdle3754;mouseout:pane.wfvdle3754"
                aria-label="Visit TRNC Ministry of Tourism's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJblFJb0FBIiwiLEFPdlZhdzJXa0YxRFlHeldEcWlLZlpkcmxmX3QsLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0lyQUlvRFEsIl0="
                href="http://www.turizm.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3745;keydown:pane.wfvdle3745;mouseover:pane.wfvdle3745;mouseout:pane.wfvdle3745"
                aria-label="Get directions to TRNC Ministry of Tourism"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJblFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3746;mouseout:pane.wfvdle3746"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Cumhuriyet Meclisi"
        href="https://www.google.com/maps/place/KKTC+Cumhuriyet+Meclisi/data=!4m7!3m6!1s0x14de17483ccdf385:0x3083068b27d60ca6!8m2!3d35.1826446!4d33.358249!16s%2Fg%2F1thjqj9g!19sChIJhfPNPEgX3hQRpgzWJ4sGgzA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3746;focus:pane.wfvdle3746;blur:pane.wfvdle3746;auxclick:pane.wfvdle3746;keydown:pane.wfvdle3746;clickmod:pane.wfvdle3746"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJd1FJb0FBIixudWxsLDEzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Cumhuriyet Meclisi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.2 stars 11 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.2</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(11)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Federal government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Bedrettin Demirel Cd</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 612 00 00</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3748;keydown:pane.wfvdle3748;mouseover:pane.wfvdle3748;mouseout:pane.wfvdle3748"
                aria-label="Visit KKTC Cumhuriyet Meclisi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJd1FJb0FBIiwiLEFPdlZhdzB1OVhVUVVoZXhUZEI3dzJUWFk4bXIsLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0kwQUlvRFEsIl0="
                href="https://cm.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3749;keydown:pane.wfvdle3749;mouseover:pane.wfvdle3749;mouseout:pane.wfvdle3749"
                aria-label="Get directions to KKTC Cumhuriyet Meclisi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJd1FJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3755;mouseout:pane.wfvdle3755"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Başbakanlık"
        href="https://www.google.com/maps/place/KKTC+Ba%C5%9Fbakanl%C4%B1k/data=!4m7!3m6!1s0x14de172d63e97b01:0x73505591a89a4c18!8m2!3d35.195683!4d33.350432!16s%2Fg%2F11b7q5l0y5!19sChIJAXvpYy0X3hQRGEyaqJFVUHM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3755;focus:pane.wfvdle3755;blur:pane.wfvdle3755;auxclick:pane.wfvdle3755;keydown:pane.wfvdle3755;clickmod:pane.wfvdle3755"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJNVFJb0FBIixudWxsLDE0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">KKTC Başbakanlık</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.0 stars 32 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(32)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Kızılay Mahallesi / Selçuklu Caddesi / Bakanlıklar
                          Yolu 3</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 31 41</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3757;keydown:pane.wfvdle3757;mouseover:pane.wfvdle3757;mouseout:pane.wfvdle3757"
                aria-label="Visit KKTC Başbakanlık's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJNVFJb0FBIiwiLEFPdlZhdzJkTnVCLTFPTlh6bDlUOVVrQmVvd0ksLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0k5QUlvRFEsIl0="
                href="http://basbakanlik.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3758;keydown:pane.wfvdle3758;mouseover:pane.wfvdle3758;mouseout:pane.wfvdle3758"
                aria-label="Get directions to KKTC Başbakanlık"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJNVFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3759;mouseout:pane.wfvdle3759"
    >
      <a
        class="hfpxzc"
        aria-label="Kktc Yayın Yüksek Kurumu"
        href="https://www.google.com/maps/place/Kktc+Yay%C4%B1n+Y%C3%BCksek+Kurumu/data=!4m7!3m6!1s0x14de17490a5587f1:0x13ecb5ba56d87ad0!8m2!3d35.1813675!4d33.3560262!16s%2Fg%2F11b7q8sj6j!19sChIJ8YdVCkkX3hQR0HrYVrq17BM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3759;focus:pane.wfvdle3759;blur:pane.wfvdle3759;auxclick:pane.wfvdle3759;keydown:pane.wfvdle3759;clickmod:pane.wfvdle3759"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJZ0FNb0FBIixudWxsLDE1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kktc Yayın Yüksek Kurumu
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3761;keydown:pane.wfvdle3761;mouseover:pane.wfvdle3761;mouseout:pane.wfvdle3761"
                aria-label="Get directions to Kktc Yayın Yüksek Kurumu"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJZ0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3762;mouseout:pane.wfvdle3762"
    >
      <a
        class="hfpxzc"
        aria-label="TRNC Ministry of Interior"
        href="https://www.google.com/maps/place/TRNC+Ministry+of+Interior/data=!4m7!3m6!1s0x14de172d8cc24569:0xc393dfaa380ddf01!8m2!3d35.1951338!4d33.3527434!16s%2Fg%2F1q627wh6q!19sChIJaUXCjC0X3hQRAd8NOKrfk8M?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3762;focus:pane.wfvdle3762;blur:pane.wfvdle3762;auxclick:pane.wfvdle3762;keydown:pane.wfvdle3762;clickmod:pane.wfvdle3762"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJa0FNb0FBIixudWxsLDE2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      TRNC Ministry of Interior
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.2 stars 127 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.2</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(127)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59W3+335</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 611 11 92</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3764;keydown:pane.wfvdle3764;mouseover:pane.wfvdle3764;mouseout:pane.wfvdle3764"
                aria-label="Visit TRNC Ministry of Interior's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJa0FNb0FBIiwiLEFPdlZhdzB0UVdqSjg3blI0WXpUaFJSR0plcm8sLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0lud01vRFEsIl0="
                href="https://icisleri.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3765;keydown:pane.wfvdle3765;mouseover:pane.wfvdle3765;mouseout:pane.wfvdle3765"
                aria-label="Get directions to TRNC Ministry of Interior"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJa0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3766;mouseout:pane.wfvdle3766"
    >
      <a
        class="hfpxzc"
        aria-label="Nicosia"
        href="https://www.google.com/maps/place/Nicosia/data=!4m7!3m6!1s0x14de1738ee0b79b1:0x3670dd21e4de669!8m2!3d35.1683821!4d33.3680646!16s%2Fg%2F11t4x4qfzv!19sChIJsXkL7jgX3hQRaeZNHtINZwM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3766;focus:pane.wfvdle3766;blur:pane.wfvdle3766;auxclick:pane.wfvdle3766;keydown:pane.wfvdle3766;clickmod:pane.wfvdle3766"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJcXdNb0FBIixudWxsLDE3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Nicosia</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Alkaiou 2-1458</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3768;keydown:pane.wfvdle3768;mouseover:pane.wfvdle3768;mouseout:pane.wfvdle3768"
                aria-label="Get directions to Nicosia"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJcXdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3769;mouseout:pane.wfvdle3769"
    >
      <a
        class="hfpxzc"
        aria-label="Immigration"
        href="https://www.google.com/maps/place/Immigration/data=!4m7!3m6!1s0x14de17dd5f8af909:0x1ee6c074f42ab3d6!8m2!3d35.1807337!4d33.3603541!16s%2Fg%2F11l795yk87!19sChIJCfmKX90X3hQR1rMq9HTA5h4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3769;focus:pane.wfvdle3769;blur:pane.wfvdle3769;auxclick:pane.wfvdle3769;keydown:pane.wfvdle3769;clickmod:pane.wfvdle3769"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJdndNb0FBIixudWxsLDE4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Immigration</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Beliğ Paşa Sk 28</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3771;keydown:pane.wfvdle3771;mouseover:pane.wfvdle3771;mouseout:pane.wfvdle3771"
                aria-label="Get directions to Immigration"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJdndNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3772;mouseout:pane.wfvdle3772"
    >
      <a
        class="hfpxzc"
        aria-label="Kıbrıs Türk Belediyeler Birliği"
        href="https://www.google.com/maps/place/K%C4%B1br%C4%B1s+T%C3%BCrk+Belediyeler+Birli%C4%9Fi/data=!4m7!3m6!1s0x14de1746bad5f693:0x82f8d19f75ac749b!8m2!3d35.1770163!4d33.3646005!16s%2Fg%2F11gh01lf0g!19sChIJk_bVukYX3hQRm3SsdZ_R-II?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3772;focus:pane.wfvdle3772;blur:pane.wfvdle3772;auxclick:pane.wfvdle3772;keydown:pane.wfvdle3772;clickmod:pane.wfvdle3772"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMEFNb0FBIixudWxsLDE5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kıbrıs Türk Belediyeler Birliği
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 2 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(2)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Kıbrıs Türk Belediyeler Birliği, Selimiye Sk</span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3774;keydown:pane.wfvdle3774;mouseover:pane.wfvdle3774;mouseout:pane.wfvdle3774"
                aria-label="Visit Kıbrıs Türk Belediyeler Birliği's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMEFNb0FBIiwiLEFPdlZhdzFObHlDYTBDNDdJWVpkS0RUbnVtSzgsLDBhaFVLRXdpbDh0N3F4WUNHQXhYaFZQRURIZGxqRExzUTYxZ0kyd01vQ1EsIl0="
                href="http://www.ktbb.org/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3775;keydown:pane.wfvdle3775;mouseover:pane.wfvdle3775;mouseout:pane.wfvdle3775"
                aria-label="Get directions to Kıbrıs Türk Belediyeler Birliği"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJMEFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3776;mouseout:pane.wfvdle3776"
    >
      <a
        class="hfpxzc"
        aria-label="Kıbrıs Türk Tütün Enstitüsü"
        href="https://www.google.com/maps/place/K%C4%B1br%C4%B1s+T%C3%BCrk+T%C3%BCt%C3%BCn+Enstit%C3%BCs%C3%BC/data=!4m7!3m6!1s0x14de1730f18246ef:0x40758ca130cc415c!8m2!3d35.19018!4d33.3580526!16s%2Fg%2F11b7p_z2qg!19sChIJ70aC8TAX3hQRXEHMMKGMdUA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3776;focus:pane.wfvdle3776;blur:pane.wfvdle3776;auxclick:pane.wfvdle3776;keydown:pane.wfvdle3776;clickmod:pane.wfvdle3776"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJNWdNb0FBIixudWxsLDIwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kıbrıs Türk Tütün Enstitüsü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 3 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(3)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59R5+36F, Atatürk Caddesi</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3778;keydown:pane.wfvdle3778;mouseover:pane.wfvdle3778;mouseout:pane.wfvdle3778"
                aria-label="Get directions to Kıbrıs Türk Tütün Enstitüsü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aWw4dDdxeFlDR0F4WGhWUEVESGRsakRMc1E4QmNJNWdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3779;mouseout:pane.wfvdle3779"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Hazine ve Muhasebe Dairesi"
        href="https://www.google.com/maps/place/KKTC+Hazine+ve+Muhasebe+Dairesi/data=!4m7!3m6!1s0x14de1737be235be7:0x16d73a3dd2679071!8m2!3d35.1846296!4d33.3583939!16s%2Fg%2F1td8099q!19sChIJ51sjvjcX3hQRcZBn0j061xY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3779;focus:pane.wfvdle3779;blur:pane.wfvdle3779;auxclick:pane.wfvdle3779;keydown:pane.wfvdle3779;clickmod:pane.wfvdle3779"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJQlNnQSIsbnVsbCwyMl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Hazine ve Muhasebe Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 4 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(4)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Ahmet Tansol Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 31 16</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3781;keydown:pane.wfvdle3781;mouseover:pane.wfvdle3781;mouseout:pane.wfvdle3781"
                aria-label="Visit KKTC Hazine ve Muhasebe Dairesi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJQlNnQSIsIixBT3ZWYXcwVjN1QXhhdV9tc09JWjE4eUh4Vkw1LCwwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE2MWdJRkNnTiwiXQ=="
                href="http://hazine.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3782;keydown:pane.wfvdle3782;mouseover:pane.wfvdle3782;mouseout:pane.wfvdle3782"
                aria-label="Get directions to KKTC Hazine ve Muhasebe Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3783;mouseout:pane.wfvdle3783"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC TSE Türk Standartları Enstitüsü"
        href="https://www.google.com/maps/place/KKTC+TSE+T%C3%BCrk+Standartlar%C4%B1+Enstit%C3%BCs%C3%BC/data=!4m7!3m6!1s0x14de174b007141e1:0xc428b25a11873596!8m2!3d35.1819178!4d33.3568623!16s%2Fg%2F11b7p_z9t1!19sChIJ4UFxAEsX3hQRljWHEVqyKMQ?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3783;focus:pane.wfvdle3783;blur:pane.wfvdle3783;auxclick:pane.wfvdle3783;keydown:pane.wfvdle3783;clickmod:pane.wfvdle3783"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJS1NnQSIsbnVsbCwyM10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC TSE Türk Standartları Enstitüsü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Osmanpaşa Cd, Şerif Arzık Sk. NO:16</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 227 96 39</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3785;keydown:pane.wfvdle3785;mouseover:pane.wfvdle3785;mouseout:pane.wfvdle3785"
                aria-label="Visit KKTC TSE Türk Standartları Enstitüsü's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJS1NnQSIsIixBT3ZWYXczeFg0QnNkdktHeV8wWDlSRmdpVVV3LCwwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE2MWdJT2lnUCwiXQ=="
                href="http://www.tse.org.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3786;keydown:pane.wfvdle3786;mouseover:pane.wfvdle3786;mouseout:pane.wfvdle3786"
                aria-label="Get directions to KKTC TSE Türk Standartları Enstitüsü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJS1NnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3787;mouseout:pane.wfvdle3787"
    >
      <a
        class="hfpxzc"
        aria-label="Nicosia Municipality Conference Room"
        href="https://www.google.com/maps/place/Nicosia+Municipality+Conference+Room/data=!4m7!3m6!1s0x14de175154895dcb:0x36ce4af81bd11ff!8m2!3d35.1733942!4d33.3657401!16s%2Fg%2F11tw_s_3g4!19sChIJy12JVFEX3hQR_xG9ga_kbAM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3787;focus:pane.wfvdle3787;blur:pane.wfvdle3787;auxclick:pane.wfvdle3787;keydown:pane.wfvdle3787;clickmod:pane.wfvdle3787"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJVHlnQSIsbnVsbCwyNF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Nicosia Municipality Conference Room
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59F8+975</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3789;keydown:pane.wfvdle3789;mouseover:pane.wfvdle3789;mouseout:pane.wfvdle3789"
                aria-label="Get directions to Nicosia Municipality Conference Room"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJVHlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3790;mouseout:pane.wfvdle3790"
    >
      <a
        class="hfpxzc"
        aria-label="Turkish Cypriot DNA Laboratory / CMPTCMO"
        href="https://www.google.com/maps/place/Turkish+Cypriot+DNA+Laboratory+%2F+CMPTCMO/data=!4m7!3m6!1s0x14de176d5b85671f:0xdc0128034ed06294!8m2!3d35.1799442!4d33.3585371!16s%2Fg%2F11tx6v3dj8!19sChIJH2eFW20X3hQRlGLQTgMoAdw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3790;focus:pane.wfvdle3790;blur:pane.wfvdle3790;auxclick:pane.wfvdle3790;keydown:pane.wfvdle3790;clickmod:pane.wfvdle3790"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJWXlnQSIsbnVsbCwyNV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Turkish Cypriot DNA Laboratory / CMPTCMO
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Tanzimat Sk 174</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3792;keydown:pane.wfvdle3792;mouseover:pane.wfvdle3792;mouseout:pane.wfvdle3792"
                aria-label="Get directions to Turkish Cypriot DNA Laboratory / CMPTCMO"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJWXlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3793;mouseout:pane.wfvdle3793"
    >
      <a
        class="hfpxzc"
        aria-label="Kktc Tarımsal Araştırma Enstitüsü Müdürlüğü"
        href="https://www.google.com/maps/place/Kktc+Tar%C4%B1msal+Ara%C5%9Ft%C4%B1rma+Enstit%C3%BCs%C3%BC+M%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC/data=!4m7!3m6!1s0x14de173ab98d0cb3:0xe3eacb0381fe806d!8m2!3d35.1843717!4d33.3577816!16s%2Fg%2F11b7q0n6q2!19sChIJswyNuToX3hQRbYD-gQPL6uM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3793;focus:pane.wfvdle3793;blur:pane.wfvdle3793;auxclick:pane.wfvdle3793;keydown:pane.wfvdle3793;clickmod:pane.wfvdle3793"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJZENnQSIsbnVsbCwyNl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kktc Tarımsal Araştırma Enstitüsü Müdürlüğü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Hasene Ilgaz Sk 1</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 02 80</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3795;keydown:pane.wfvdle3795;mouseover:pane.wfvdle3795;mouseout:pane.wfvdle3795"
                aria-label="Visit Kktc Tarımsal Araştırma Enstitüsü Müdürlüğü's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJZENnQSIsIixBT3ZWYXcyY01xMzBvV2hXMDM4aHlVaFljQ2hvLCwwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE2MWdJZ1FFb0RBLCJd"
                href="https://tae.gov.ct.tr/%C4%B0LET%C4%B0%C5%9E%C4%B0M"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3796;keydown:pane.wfvdle3796;mouseover:pane.wfvdle3796;mouseout:pane.wfvdle3796"
                aria-label="Get directions to Kktc Tarımsal Araştırma Enstitüsü Müdürlüğü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJZENnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3797;mouseout:pane.wfvdle3797"
    >
      <a
        class="hfpxzc"
        aria-label="Presidential Palace"
        href="https://www.google.com/maps/place/Presidential+Palace/data=!4m7!3m6!1s0x14de1747de6e4117:0x4ea30776d3d1882e!8m2!3d35.1809513!4d33.3595821!16s%2Fg%2F11cmg4w3n9!19sChIJF0Fu3kcX3hQRLojR03YHo04?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3797;focus:pane.wfvdle3797;blur:pane.wfvdle3797;auxclick:pane.wfvdle3797;keydown:pane.wfvdle3797;clickmod:pane.wfvdle3797"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJaWdFb0FBIixudWxsLDI3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Presidential Palace
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.3 stars 10 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.3</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(10)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59J5+9RP, Selahattin Sonat Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5 PM</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3799;keydown:pane.wfvdle3799;mouseover:pane.wfvdle3799;mouseout:pane.wfvdle3799"
                aria-label="Get directions to Presidential Palace"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJaWdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3800;mouseout:pane.wfvdle3800"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Orman Dairesi Müdürlüğü"
        href="https://www.google.com/maps/place/KKTC+Orman+Dairesi+M%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC/data=!4m7!3m6!1s0x14de1731c9ce1479:0xa9e48f09af376581!8m2!3d35.1923717!4d33.3565313!16s%2Fg%2F1td8ff8b!19sChIJeRTOyTEX3hQRgWU3rwmP5Kk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3800;focus:pane.wfvdle3800;blur:pane.wfvdle3800;auxclick:pane.wfvdle3800;keydown:pane.wfvdle3800;clickmod:pane.wfvdle3800"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJckFFb0FBIixudWxsLDI4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Orman Dairesi Müdürlüğü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 4 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(4)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Şehit Ecvet Yusuf Caddesi NO:16</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 444 01 77</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3802;keydown:pane.wfvdle3802;mouseover:pane.wfvdle3802;mouseout:pane.wfvdle3802"
                aria-label="Visit KKTC Orman Dairesi Müdürlüğü's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJckFFb0FBIiwiLEFPdlZhdzJfbW5kT25ackxaVVRjOTNWVGlHMFosLDBhaFVLRXdqemp0UHJ4WUNHQXhYT1JQRURIWk4zQTFZUTYxZ0l1d0VvRFEsIl0="
                href="http://www.orman.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3803;keydown:pane.wfvdle3803;mouseover:pane.wfvdle3803;mouseout:pane.wfvdle3803"
                aria-label="Get directions to KKTC Orman Dairesi Müdürlüğü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJckFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3804;mouseout:pane.wfvdle3804"
    >
      <a
        class="hfpxzc"
        aria-label="TRNC Social Insurance Office"
        href="https://www.google.com/maps/place/TRNC+Social+Insurance+Office/data=!4m7!3m6!1s0x14de1736eb394bd5:0x503903bf52afee5c!8m2!3d35.187497!4d33.3557316!16s%2Fg%2F11b7q7pkmq!19sChIJ1Us56zYX3hQRXO6vUr8DOVA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3804;focus:pane.wfvdle3804;blur:pane.wfvdle3804;auxclick:pane.wfvdle3804;keydown:pane.wfvdle3804;clickmod:pane.wfvdle3804"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJMEFFb0FBIixudWxsLDI5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      TRNC Social Insurance Office
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.9 stars 28 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.9</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(28)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Bedrettin Demirel Caddesi</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 31 81</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3806;keydown:pane.wfvdle3806;mouseover:pane.wfvdle3806;mouseout:pane.wfvdle3806"
                aria-label="Visit TRNC Social Insurance Office's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJMEFFb0FBIiwiLEFPdlZhdzAtWVFuRXNwekl5alJTbUM2eVBEQXosLDBhaFVLRXdqemp0UHJ4WUNHQXhYT1JQRURIWk4zQTFZUTYxZ0kzd0VvRFEsIl0="
                href="https://ssd.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3807;keydown:pane.wfvdle3807;mouseover:pane.wfvdle3807;mouseout:pane.wfvdle3807"
                aria-label="Get directions to TRNC Social Insurance Office"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJMEFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3808;mouseout:pane.wfvdle3808"
    >
      <a
        class="hfpxzc"
        aria-label="Kültür Dairesi Müdürlüğü"
        href="https://www.google.com/maps/place/K%C3%BClt%C3%BCr+Dairesi+M%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC/data=!4m7!3m6!1s0x14de17377cefb97d:0x29c80e1bc7f7a532!8m2!3d35.185766!4d33.35961!16s%2Fg%2F11b7q5x14k!19sChIJfbnvfDcX3hQRMqX3xxsOyCk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3808;focus:pane.wfvdle3808;blur:pane.wfvdle3808;auxclick:pane.wfvdle3808;keydown:pane.wfvdle3808;clickmod:pane.wfvdle3808"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJOUFFb0FBIixudWxsLDMwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kültür Dairesi Müdürlüğü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59P5+8R5, Kızılay Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3810;keydown:pane.wfvdle3810;mouseover:pane.wfvdle3810;mouseout:pane.wfvdle3810"
                aria-label="Get directions to Kültür Dairesi Müdürlüğü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJOUFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3811;mouseout:pane.wfvdle3811"
    >
      <a
        class="hfpxzc"
        aria-label="وزارة الأقتصاد"
        href="https://www.google.com/maps/place/%D9%88%D8%B2%D8%A7%D8%B1%D8%A9+%D8%A7%D9%84%D8%A3%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%E2%80%AD/data=!4m7!3m6!1s0x14de177b580e62ed:0xdb4b1e6e4b892bee!8m2!3d35.1848515!4d33.3575144!16s%2Fg%2F11ty0w9wn7!19sChIJ7WIOWHsX3hQR7iuJS24eS9s?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3811;focus:pane.wfvdle3811;blur:pane.wfvdle3811;auxclick:pane.wfvdle3811;keydown:pane.wfvdle3811;clickmod:pane.wfvdle3811"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJaWdJb0FBIixudWxsLDMxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      <span dir="rtl">وزارة الأقتصاد</span>
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>H. Ilgaz Sk 23</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3813;keydown:pane.wfvdle3813;mouseover:pane.wfvdle3813;mouseout:pane.wfvdle3813"
                aria-label="Get directions to وزارة الأقتصاد"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJaWdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3814;mouseout:pane.wfvdle3814"
    >
      <a
        class="hfpxzc"
        aria-label="Trt Kıbrıs Haber Bürosu"
        href="https://www.google.com/maps/place/Trt+K%C4%B1br%C4%B1s+Haber+B%C3%BCrosu/data=!4m7!3m6!1s0x14de174a4aea674b:0xae70874843c52bb5!8m2!3d35.18259!4d33.352723!16s%2Fg%2F11b7p_g8m6!19sChIJS2fqSkoX3hQRtSvFQ0iHcK4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3814;focus:pane.wfvdle3814;blur:pane.wfvdle3814;auxclick:pane.wfvdle3814;keydown:pane.wfvdle3814;clickmod:pane.wfvdle3814"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJbXdJb0FBIixudWxsLDMyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Trt Kıbrıs Haber Bürosu
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59M3+23Q, Osmanpaşa Cd</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3816;keydown:pane.wfvdle3816;mouseover:pane.wfvdle3816;mouseout:pane.wfvdle3816"
                aria-label="Get directions to Trt Kıbrıs Haber Bürosu"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJbXdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3817;mouseout:pane.wfvdle3817"
    >
      <a
        class="hfpxzc"
        aria-label="The House of the Citizen"
        href="https://www.google.com/maps/place/The+House+of+the+Citizen/data=!4m7!3m6!1s0x14de170e9660d1c9:0xf9dadffcf8f0a8f6!8m2!3d35.1717091!4d33.355819!16s%2Fg%2F11tdr_tks3!19sChIJydFglg4X3hQR9qjw-Pzf2vk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3817;focus:pane.wfvdle3817;blur:pane.wfvdle3817;auxclick:pane.wfvdle3817;keydown:pane.wfvdle3817;clickmod:pane.wfvdle3817"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJcmdJb0FBIixudWxsLDMzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      The House of the Citizen
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Mouseiou 1</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3819;keydown:pane.wfvdle3819;mouseover:pane.wfvdle3819;mouseout:pane.wfvdle3819"
                aria-label="Get directions to The House of the Citizen"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJcmdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3820;mouseout:pane.wfvdle3820"
    >
      <a
        class="hfpxzc"
        aria-label="TRNC Ministry of Finance"
        href="https://www.google.com/maps/place/TRNC+Ministry+of+Finance/data=!4m7!3m6!1s0x14de1737b9bc415f:0xb7c293cc879208cb!8m2!3d35.184803!4d33.357849!16s%2Fg%2F11b7q590l3!19sChIJX0G8uTcX3hQRywiSh8yTwrc?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3820;focus:pane.wfvdle3820;blur:pane.wfvdle3820;auxclick:pane.wfvdle3820;keydown:pane.wfvdle3820;clickmod:pane.wfvdle3820"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJeFFJb0FBIixudWxsLDM0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      TRNC Ministry of Finance
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.9 stars 20 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.9</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(20)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Hasene Ilgaz Sokak</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 31 16</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3822;keydown:pane.wfvdle3822;mouseover:pane.wfvdle3822;mouseout:pane.wfvdle3822"
                aria-label="Visit TRNC Ministry of Finance's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJeFFJb0FBIiwiLEFPdlZhdzJlSGg2c2t0M3ZuYnR0YWpwaTl4WUQsLDBhaFVLRXdqemp0UHJ4WUNHQXhYT1JQRURIWk4zQTFZUTYxZ0kxUUlvRGcsIl0="
                href="http://www.kktcmaliye.com/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3823;keydown:pane.wfvdle3823;mouseover:pane.wfvdle3823;mouseout:pane.wfvdle3823"
                aria-label="Get directions to TRNC Ministry of Finance"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJeFFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3824;mouseout:pane.wfvdle3824"
    >
      <a
        class="hfpxzc"
        aria-label="İçişleri Ve Yerel Yönetimler Bakanlığı Lefkoşa Kaymakamlığı"
        href="https://www.google.com/maps/place/%C4%B0%C3%A7i%C5%9Fleri+Ve+Yerel+Y%C3%B6netimler+Bakanl%C4%B1%C4%9F%C4%B1+Lefko%C5%9Fa+Kaymakaml%C4%B1%C4%9F%C4%B1/data=!4m7!3m6!1s0x14de172359ba671f:0x94fda8073a306b8b!8m2!3d35.191432!4d33.365671!16s%2Fg%2F11b7q1s2k0!19sChIJH2e6WSMX3hQRi2swOgeo_ZQ?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3824;focus:pane.wfvdle3824;blur:pane.wfvdle3824;auxclick:pane.wfvdle3824;keydown:pane.wfvdle3824;clickmod:pane.wfvdle3824"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJNFFJb0FBIixudWxsLDM1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      İçişleri Ve Yerel Yönetimler Bakanlığı Lefkoşa
                      Kaymakamlığı
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.8 stars 4 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.8</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(4)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59R8+H7F, Okullar Yolu Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3826;keydown:pane.wfvdle3826;mouseover:pane.wfvdle3826;mouseout:pane.wfvdle3826"
                aria-label="Get directions to İçişleri Ve Yerel Yönetimler Bakanlığı Lefkoşa Kaymakamlığı"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJNFFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3827;mouseout:pane.wfvdle3827"
    >
      <a
        class="hfpxzc"
        aria-label="مبنا48"
        href="https://www.google.com/maps/place/%D9%85%D8%A8%D9%86%D8%A748%E2%80%AD/data=!4m7!3m6!1s0x14de17919ab02bc3:0xa39747ec4715e848!8m2!3d35.1689902!4d33.3549131!16s%2Fg%2F11l5kbq3y7!19sChIJwyuwmpEX3hQRSOgVR-xHl6M?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3827;focus:pane.wfvdle3827;blur:pane.wfvdle3827;auxclick:pane.wfvdle3827;keydown:pane.wfvdle3827;clickmod:pane.wfvdle3827"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJLVFJb0FBIixudWxsLDM2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      <span dir="rtl">مبنا48</span>
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5993+HXV</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3829;keydown:pane.wfvdle3829;mouseover:pane.wfvdle3829;mouseout:pane.wfvdle3829"
                aria-label="Get directions to مبنا48"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJLVFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3830;mouseout:pane.wfvdle3830"
    >
      <a
        class="hfpxzc"
        aria-label="Cyprus Research Centre - Κέντρο Επιστημονικών Ερευνών"
        href="https://www.google.com/maps/place/Cyprus+Research+Centre+-+%CE%9A%CE%AD%CE%BD%CF%84%CF%81%CE%BF+%CE%95%CF%80%CE%B9%CF%83%CF%84%CE%B7%CE%BC%CE%BF%CE%BD%CE%B9%CE%BA%CF%8E%CE%BD+%CE%95%CF%81%CE%B5%CF%85%CE%BD%CF%8E%CE%BD/data=!4m7!3m6!1s0x14de1789c2f09bcd:0xdbaca6640b24dd84!8m2!3d35.1704906!4d33.3539468!16s%2Fg%2F11r9714r9f!19sChIJzZvwwokX3hQRhN0kC2SmrNs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3830;focus:pane.wfvdle3830;blur:pane.wfvdle3830;auxclick:pane.wfvdle3830;keydown:pane.wfvdle3830;clickmod:pane.wfvdle3830"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJalFNb0FBIixudWxsLDM3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Cyprus Research Centre - Κέντρο Επιστημονικών Ερευνών
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59C3+5HW Gladstone 6</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 456320</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3832;keydown:pane.wfvdle3832;mouseover:pane.wfvdle3832;mouseout:pane.wfvdle3832"
                aria-label="Visit Cyprus Research Centre - Κέντρο Επιστημονικών Ερευνών's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJalFNb0FBIiwiLEFPdlZhdzFHYWJJZW1LenlxNmJxZE8yLTVCOFQsLDBhaFVLRXdqemp0UHJ4WUNHQXhYT1JQRURIWk4zQTFZUTYxZ0luZ01vRUEsIl0="
                href="http://www.moec.gov.cy/kee/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3833;keydown:pane.wfvdle3833;mouseover:pane.wfvdle3833;mouseout:pane.wfvdle3833"
                aria-label="Get directions to Cyprus Research Centre - Κέντρο Επιστημονικών Ερευνών"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJalFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3834;mouseout:pane.wfvdle3834"
    >
      <a
        class="hfpxzc"
        aria-label='Αίθουσα Εκδηλώσεων "Θεόφιλος Γεωργιάδης" - Γραφείο Τύπου και Πληροφοριών'
        href="https://www.google.com/maps/place/%CE%91%CE%AF%CE%B8%CE%BF%CF%85%CF%83%CE%B1+%CE%95%CE%BA%CE%B4%CE%B7%CE%BB%CF%8E%CF%83%CE%B5%CF%89%CE%BD+%22%CE%98%CE%B5%CF%8C%CF%86%CE%B9%CE%BB%CE%BF%CF%82+%CE%93%CE%B5%CF%89%CF%81%CE%B3%CE%B9%CE%AC%CE%B4%CE%B7%CF%82%22+-+%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF+%CE%A4%CF%8D%CF%80%CE%BF%CF%85+%CE%BA%CE%B1%CE%B9+%CE%A0%CE%BB%CE%B7%CF%81%CE%BF%CF%86%CE%BF%CF%81%CE%B9%CF%8E%CE%BD/data=!4m7!3m6!1s0x14de1933771863bd:0xeb483231730d8d!8m2!3d35.1588482!4d33.3515776!16s%2Fg%2F11v9s43637!19sChIJvWMYdzMZ3hQRjQ1zMTJI6wA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3834;focus:pane.wfvdle3834;blur:pane.wfvdle3834;auxclick:pane.wfvdle3834;keydown:pane.wfvdle3834;clickmod:pane.wfvdle3834"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJc1FNb0FBIixudWxsLDM4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Αίθουσα Εκδηλώσεων "Θεόφιλος Γεωργιάδης" - Γραφείο Τύπου
                      και Πληροφοριών
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5952+GH5, Kyriakou Matsi</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3836;keydown:pane.wfvdle3836;mouseover:pane.wfvdle3836;mouseout:pane.wfvdle3836"
                aria-label='Get directions to Αίθουσα Εκδηλώσεων "Θεόφιλος Γεωργιάδης" - Γραφείο Τύπου και Πληροφοριών'
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJc1FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3837;mouseout:pane.wfvdle3837"
    >
      <a
        class="hfpxzc"
        aria-label="Başsavcılık Binası"
        href="https://www.google.com/maps/place/Ba%C5%9Fsavc%C4%B1l%C4%B1k+Binas%C4%B1/data=!4m7!3m6!1s0x14de17777a47c07f:0x9436cf5630662589!8m2!3d35.1786388!4d33.3600976!16s%2Fg%2F11t0swch5l!19sChIJf8BHencX3hQRiSVmMFbPNpQ?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3837;focus:pane.wfvdle3837;blur:pane.wfvdle3837;auxclick:pane.wfvdle3837;keydown:pane.wfvdle3837;clickmod:pane.wfvdle3837"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJeHdNb0FBIixudWxsLDM5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Başsavcılık Binası
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59H6+F25</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3839;keydown:pane.wfvdle3839;mouseover:pane.wfvdle3839;mouseout:pane.wfvdle3839"
                aria-label="Get directions to Başsavcılık Binası"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJeHdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3840;mouseout:pane.wfvdle3840"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Ombudsman"
        href="https://www.google.com/maps/place/KKTC+Ombudsman/data=!4m7!3m6!1s0x14de17a57652944b:0x793b498e72e2be54!8m2!3d35.1811773!4d33.3637141!16s%2Fg%2F11fn4346yh!19sChIJS5RSdqUX3hQRVL7ico5JO3k?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3840;focus:pane.wfvdle3840;blur:pane.wfvdle3840;auxclick:pane.wfvdle3840;keydown:pane.wfvdle3840;clickmod:pane.wfvdle3840"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJMndNb0FBIixudWxsLDQwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">KKTC Ombudsman</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Celaliye Sk No: 2</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3842;keydown:pane.wfvdle3842;mouseover:pane.wfvdle3842;mouseout:pane.wfvdle3842"
                aria-label="Get directions to KKTC Ombudsman"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJMndNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3843;mouseout:pane.wfvdle3843"
    >
      <a
        class="hfpxzc"
        aria-label="Tax Department"
        href="https://www.google.com/maps/place/Tax+Department/data=!4m7!3m6!1s0x14de176c701fb27b:0x9b3623c9e853f046!8m2!3d35.167007!4d33.3546155!16s%2Fg%2F11p653k0_d!19sChIJe7IfcGwX3hQRRvBT6MkjNps?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3843;focus:pane.wfvdle3843;blur:pane.wfvdle3843;auxclick:pane.wfvdle3843;keydown:pane.wfvdle3843;clickmod:pane.wfvdle3843"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJOFFNb0FBIixudWxsLDQxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Tax Department</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Michalaki Karaoli &amp; Gregory Afxentiou
                          Nicosia</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 602723</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3845;keydown:pane.wfvdle3845;mouseover:pane.wfvdle3845;mouseout:pane.wfvdle3845"
                aria-label="Get directions to Tax Department"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3anpqdFByeFlDR0F4WE9SUEVESFpOM0ExWVE4QmNJOFFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3846;mouseout:pane.wfvdle3846"
    >
      <a
        class="hfpxzc"
        aria-label="European Union Coordination Center"
        href="https://www.google.com/maps/place/European+Union+Coordination+Center/data=!4m7!3m6!1s0x14de1745dbd726e5:0x6bfc82a048d3b631!8m2!3d35.1769501!4d33.3617315!16s%2Fg%2F1pv2v0lw9!19sChIJ5SbX20UX3hQRMbbTSKCC_Gs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3846;focus:pane.wfvdle3846;blur:pane.wfvdle3846;auxclick:pane.wfvdle3846;keydown:pane.wfvdle3846;clickmod:pane.wfvdle3846"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJQlNnQSIsbnVsbCw0M10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      European Union Coordination Center
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59G6+QMQ, İrfan Bey Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 227 37 35</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3848;keydown:pane.wfvdle3848;mouseover:pane.wfvdle3848;mouseout:pane.wfvdle3848"
                aria-label="Get directions to European Union Coordination Center"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3849;mouseout:pane.wfvdle3849"
    >
      <a
        class="hfpxzc"
        aria-label="Devlet Emlak ve Malzeme Dairesi"
        href="https://www.google.com/maps/place/Devlet+Emlak+ve+Malzeme+Dairesi/data=!4m7!3m6!1s0x14de1739c0a4a2ed:0x668e0ba5abcd100e!8m2!3d35.1857424!4d33.3612005!16s%2Fg%2F11f57ty9yb!19sChIJ7aKkwDkX3hQRDhDNq6ULjmY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3849;focus:pane.wfvdle3849;blur:pane.wfvdle3849;auxclick:pane.wfvdle3849;keydown:pane.wfvdle3849;clickmod:pane.wfvdle3849"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJSHlnQSIsbnVsbCw0NF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Devlet Emlak ve Malzeme Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59P6+7FW</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3851;keydown:pane.wfvdle3851;mouseover:pane.wfvdle3851;mouseout:pane.wfvdle3851"
                aria-label="Visit Devlet Emlak ve Malzeme Dairesi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJSHlnQSIsIixBT3ZWYXcyQWVxLUdkTkRRbTNBbjVmVVVzNWpOLCwwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE2MWdJS2lnSiwiXQ=="
                href="http://www.dem.gov.ct.tr///"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3852;keydown:pane.wfvdle3852;mouseover:pane.wfvdle3852;mouseout:pane.wfvdle3852"
                aria-label="Get directions to Devlet Emlak ve Malzeme Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJSHlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3853;mouseout:pane.wfvdle3853"
    >
      <a
        class="hfpxzc"
        aria-label="Union of Cyprus Municipalities"
        href="https://www.google.com/maps/place/Union+of+Cyprus+Municipalities/data=!4m7!3m6!1s0x14de17674ace37d3:0xb54861de1e6fcbdd!8m2!3d35.1724712!4d33.3577477!16s%2Fg%2F11t1fcywk5!19sChIJ0zfOSmcX3hQR3ctvHt5hSLU?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3853;focus:pane.wfvdle3853;blur:pane.wfvdle3853;auxclick:pane.wfvdle3853;keydown:pane.wfvdle3853;clickmod:pane.wfvdle3853"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJTmlnQSIsbnVsbCw0NV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Union of Cyprus Municipalities
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>County government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Rigenis 78</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 445170</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3855;keydown:pane.wfvdle3855;mouseover:pane.wfvdle3855;mouseout:pane.wfvdle3855"
                aria-label="Visit Union of Cyprus Municipalities's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJTmlnQSIsIixBT3ZWYXcwRTBTaF9ZQmhSWjRtYk53TDJtX2szLCwwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE2MWdJUmlnUCwiXQ=="
                href="https://ucm.org.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3856;keydown:pane.wfvdle3856;mouseover:pane.wfvdle3856;mouseout:pane.wfvdle3856"
                aria-label="Get directions to Union of Cyprus Municipalities"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJTmlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3857;mouseout:pane.wfvdle3857"
    >
      <a
        class="hfpxzc"
        aria-label="Agricultural Chamber of Cyprus"
        href="https://www.google.com/maps/place/Agricultural+Chamber+of+Cyprus/data=!4m7!3m6!1s0x14de175c68d92265:0x7cc852e72f3dd6d2!8m2!3d35.1673067!4d33.3662879!16s%2Fg%2F11c4874r1v!19sChIJZSLZaFwX3hQR0tY9L-dSyHw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3857;focus:pane.wfvdle3857;blur:pane.wfvdle3857;auxclick:pane.wfvdle3857;keydown:pane.wfvdle3857;clickmod:pane.wfvdle3857"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJWENnQSIsbnVsbCw0Nl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Agricultural Chamber of Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Medontos 9</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3859;keydown:pane.wfvdle3859;mouseover:pane.wfvdle3859;mouseout:pane.wfvdle3859"
                aria-label="Get directions to Agricultural Chamber of Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJWENnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3860;mouseout:pane.wfvdle3860"
    >
      <a
        class="hfpxzc"
        aria-label="π.ο.π.ο"
        href="https://www.google.com/maps/place/%CF%80.%CE%BF.%CF%80.%CE%BF/data=!4m7!3m6!1s0x14de1784f6682a07:0x286744177831bfef!8m2!3d35.1686452!4d33.3682504!16s%2Fg%2F11hw7ftqp3!19sChIJBypo9oQX3hQR778xeBdEZyg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3860;focus:pane.wfvdle3860;blur:pane.wfvdle3860;auxclick:pane.wfvdle3860;keydown:pane.wfvdle3860;clickmod:pane.wfvdle3860"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJY3lnQSIsbnVsbCw0N10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">π.ο.π.ο</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 2 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(2)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Alkaiou 1</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 818518</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3862;keydown:pane.wfvdle3862;mouseover:pane.wfvdle3862;mouseout:pane.wfvdle3862"
                aria-label="Get directions to π.ο.π.ο"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJY3lnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3863;mouseout:pane.wfvdle3863"
    >
      <a
        class="hfpxzc"
        aria-label="Public Service Commission"
        href="https://www.google.com/maps/place/Public+Service+Commission/data=!4m7!3m6!1s0x14de1755c68ee363:0xda064fa4fbde73b9!8m2!3d35.1674297!4d33.3537447!16s%2Fg%2F11g81s88q5!19sChIJY-OOxlUX3hQRuXPe-6RPBto?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3863;focus:pane.wfvdle3863;blur:pane.wfvdle3863;auxclick:pane.wfvdle3863;keydown:pane.wfvdle3863;clickmod:pane.wfvdle3863"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbWdFb0FBIixudWxsLDQ4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Public Service Commission
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.4 stars 9 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.4</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(9)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5983+XFH, Michael Karaoli</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 602571</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3865;keydown:pane.wfvdle3865;mouseover:pane.wfvdle3865;mouseout:pane.wfvdle3865"
                aria-label="Visit Public Service Commission's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbWdFb0FBIiwiLEFPdlZhdzNkY0UtbzVzT3Z0UjRlZmVRckM5WXYsLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0lyZ0VvRWcsIl0="
                href="http://www.psc.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3866;keydown:pane.wfvdle3866;mouseover:pane.wfvdle3866;mouseout:pane.wfvdle3866"
                aria-label="Get directions to Public Service Commission"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbWdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3867;mouseout:pane.wfvdle3867"
    >
      <a
        class="hfpxzc"
        aria-label="Citizens' Service Center"
        href="https://www.google.com/maps/place/Citizens%27+Service+Center/data=!4m7!3m6!1s0x14de19fd06a7245b:0xe6053808556e0973!8m2!3d35.1660468!4d33.3620798!16s%2Fg%2F1vtkr95w!19sChIJWySnBv0Z3hQRcwluVQg4BeY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3867;focus:pane.wfvdle3867;blur:pane.wfvdle3867;auxclick:pane.wfvdle3867;keydown:pane.wfvdle3867;clickmod:pane.wfvdle3867"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJeEFFb0FBIixudWxsLDQ5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Citizens' Service Center
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.9 stars 98 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.9</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(98)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Λεωφ. Αρχιεπισκόπου Μακαρίου Γ' 36</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 309100</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3870;keydown:pane.wfvdle3870;mouseover:pane.wfvdle3870;mouseout:pane.wfvdle3870"
                aria-label="Visit Citizens' Service Center's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJeEFFb0FBIiwiLEFPdlZhdzM4RUx0VnhSVVp6bFhSNFpHdnBUNWcsLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0kxUUVvRHcsIl0="
                href="http://www.mof.gov.cy/mof/papd/papd.nsf/page50_gr/page50_gr?OpenDocument#"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3871;keydown:pane.wfvdle3871;mouseover:pane.wfvdle3871;mouseout:pane.wfvdle3871"
                aria-label="Get directions to Citizens' Service Center"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJeEFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue">
          <div class="AyRUI" role="presentation" style="height: 8px">
            &nbsp;
          </div>
          <div class="n8sPKe ccePVe">
            <div class="Ahnjwc fontBodyMedium">
              <div class="W6VQef">
                <div
                  aria-hidden="true"
                  class="JoXfOb fCbqBc"
                  style="width: 16px; height: 16px"
                >
                  <img
                    alt=""
                    class="Jn12ke xcEj5d"
                    src="https://ssl.gstatic.com/local/servicebusiness/default_user.png"
                    style="width: 16px; height: 16px"
                  />
                </div>
                <div class="ah5Ghc">
                  <span style="font-weight: 400"
                    >"I swear KEP is what's holding all the government services
                    together."</span
                  >
                </div>
              </div>
              <div class="Q4BGF"></div>
            </div>
          </div>
        </div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3872;mouseout:pane.wfvdle3872"
    >
      <a
        class="hfpxzc"
        aria-label="Karayolları Dairesi Müdürlüğü"
        href="https://www.google.com/maps/place/Karayollar%C4%B1+Dairesi+M%C3%BCd%C3%BCrl%C3%BC%C4%9F%C3%BC/data=!4m7!3m6!1s0x14de1738dc1c6faf:0xad6e98348f8eb7d9!8m2!3d35.1834933!4d33.3643319!16s%2Fg%2F11bycfq7n2!19sChIJr28c3DgX3hQR2beOjzSYbq0?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3872;focus:pane.wfvdle3872;blur:pane.wfvdle3872;auxclick:pane.wfvdle3872;keydown:pane.wfvdle3872;clickmod:pane.wfvdle3872"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJN0FFb0FBIixudWxsLDUwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Karayolları Dairesi Müdürlüğü
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59M7+9PW, Kaymaklı Yolu Sokak</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3874;keydown:pane.wfvdle3874;mouseover:pane.wfvdle3874;mouseout:pane.wfvdle3874"
                aria-label="Get directions to Karayolları Dairesi Müdürlüğü"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJN0FFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3875;mouseout:pane.wfvdle3875"
    >
      <a
        class="hfpxzc"
        aria-label="Επαρχιακό Γραφείο Εργασίας"
        href="https://www.google.com/maps/place/%CE%95%CF%80%CE%B1%CF%81%CF%87%CE%B9%CE%B1%CE%BA%CF%8C+%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF+%CE%95%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de17006a948435:0xeec0be12947a723c!8m2!3d35.172447!4d33.3560303!16s%2Fg%2F11vwqsw7_7!19sChIJNYSUagAX3hQRPHJ6lBK-wO4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3875;focus:pane.wfvdle3875;blur:pane.wfvdle3875;auxclick:pane.wfvdle3875;keydown:pane.wfvdle3875;clickmod:pane.wfvdle3875"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJZ2dJb0FBIixudWxsLDUxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Επαρχιακό Γραφείο Εργασίας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Mouseiou 3</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3877;keydown:pane.wfvdle3877;mouseover:pane.wfvdle3877;mouseout:pane.wfvdle3877"
                aria-label="Get directions to Επαρχιακό Γραφείο Εργασίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJZ2dJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3878;mouseout:pane.wfvdle3878"
    >
      <a
        class="hfpxzc"
        aria-label="Lefkoşa İlçe Seçim Kurulu"
        href="https://www.google.com/maps/place/Lefko%C5%9Fa+%C4%B0l%C3%A7e+Se%C3%A7im+Kurulu/data=!4m7!3m6!1s0x14de174615cc17d3:0x39ae36bb2b6c0d1b!8m2!3d35.1786!4d33.360949!16s%2Fg%2F11b7q8gstj!19sChIJ0xfMFUYX3hQRGw1sK7s2rjk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3878;focus:pane.wfvdle3878;blur:pane.wfvdle3878;auxclick:pane.wfvdle3878;keydown:pane.wfvdle3878;clickmod:pane.wfvdle3878"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbGdJb0FBIixudWxsLDUyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Lefkoşa İlçe Seçim Kurulu
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3880;keydown:pane.wfvdle3880;mouseover:pane.wfvdle3880;mouseout:pane.wfvdle3880"
                aria-label="Get directions to Lefkoşa İlçe Seçim Kurulu"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbGdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3881;mouseout:pane.wfvdle3881"
    >
      <a
        class="hfpxzc"
        aria-label="Post Office"
        href="https://www.google.com/maps/place/Post+Office/data=!4m7!3m6!1s0x14de1746020e3a2b:0xcd1b9e2f31a76fd6!8m2!3d35.178272!4d33.359889!16s%2Fg%2F1tg97_tw!19sChIJKzoOAkYX3hQR1m-nMS-eG80?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3881;focus:pane.wfvdle3881;blur:pane.wfvdle3881;auxclick:pane.wfvdle3881;keydown:pane.wfvdle3881;clickmod:pane.wfvdle3881"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJcGdJb0FBIixudWxsLDUzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Post Office</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.3 stars 39 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.3</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(39)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Post office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59H5+8X2, Posta Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:15 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 59 82</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3884;keydown:pane.wfvdle3884;mouseover:pane.wfvdle3884;mouseout:pane.wfvdle3884"
                aria-label="Visit Post Office's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJcGdJb0FBIiwiLEFPdlZhdzE1YlBpSTVLdjJlaVlsYkxUWDVuSXksLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0l0d0lvRHcsIl0="
                href="http://www.posta.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3885;keydown:pane.wfvdle3885;mouseover:pane.wfvdle3885;mouseout:pane.wfvdle3885"
                aria-label="Get directions to Post Office"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJcGdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue">
          <div class="AyRUI" role="presentation" style="height: 8px">
            &nbsp;
          </div>
          <div class="n8sPKe ccePVe">
            <div class="Ahnjwc fontBodyMedium">
              <div class="W6VQef">
                <div
                  aria-hidden="true"
                  class="JoXfOb fCbqBc"
                  style="width: 16px; height: 16px"
                >
                  <img
                    alt=""
                    class="Jn12ke xcEj5d"
                    src="https://ssl.gstatic.com/local/servicebusiness/default_user.png"
                    style="width: 16px; height: 16px"
                  />
                </div>
                <div class="ah5Ghc">
                  <span style="font-weight: 400">"... Cyprus Island </span
                  ><span style="font-weight: 500">Gov</span
                  ><span style="font-weight: 400">
                    then became TRNC Post Head Office in 1984."</span
                  >
                </div>
              </div>
              <div class="Q4BGF"></div>
            </div>
          </div>
        </div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3886;mouseout:pane.wfvdle3886"
    >
      <a
        class="hfpxzc"
        aria-label="Cyprus Securities and Exchange Commission (CySEC)"
        href="https://www.google.com/maps/place/Cyprus+Securities+and+Exchange+Commission+%28CySEC%29/data=!4m7!3m6!1s0x14de1750d0842b23:0xe0f001912beb47a0!8m2!3d35.1693683!4d33.3575315!16s%2Fg%2F11c2klmfhy!19sChIJIyuE0FAX3hQRoEfrK5EB8OA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3886;focus:pane.wfvdle3886;blur:pane.wfvdle3886;auxclick:pane.wfvdle3886;keydown:pane.wfvdle3886;clickmod:pane.wfvdle3886"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJendJb0FBIixudWxsLDU0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Cyprus Securities and Exchange Commission (CySEC)
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.0 stars 3 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(3)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>19 Diagorou Str. CY-1097</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="font-weight: 400; color: rgba(176, 96, 0, 1)"
                            >Closes soon</span
                          ><span style="font-weight: 400">
                            ⋅ 4 PM ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 506600</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3888;keydown:pane.wfvdle3888;mouseover:pane.wfvdle3888;mouseout:pane.wfvdle3888"
                aria-label="Visit Cyprus Securities and Exchange Commission (CySEC)'s website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJendJb0FBIiwiLEFPdlZhdzFWNmRpMkNSWDZUQWVIMHdtd1g2Q1AsLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0k0QUlvRHcsIl0="
                href="https://www.cysec.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3889;keydown:pane.wfvdle3889;mouseover:pane.wfvdle3889;mouseout:pane.wfvdle3889"
                aria-label="Get directions to Cyprus Securities and Exchange Commission (CySEC)"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJendJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3890;mouseout:pane.wfvdle3890"
    >
      <a
        class="hfpxzc"
        aria-label="Directorate General for Growth, Ministry of Finance"
        href="https://www.google.com/maps/place/Directorate+General+for+Growth,+Ministry+of+Finance/data=!4m7!3m6!1s0x14de17a4329dc107:0x9fcb71de5012178!8m2!3d35.1680576!4d33.3538122!16s%2Fg%2F11h5sqm2j7!19sChIJB8GdMqQX3hQReCEB5R23_Ak?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3890;focus:pane.wfvdle3890;blur:pane.wfvdle3890;auxclick:pane.wfvdle3890;keydown:pane.wfvdle3890;clickmod:pane.wfvdle3890"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJOVFJb0FBIixudWxsLDU1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Directorate General for Growth, Ministry of Finance
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Lordou Vyronos 29</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="font-weight: 400; color: rgba(176, 96, 0, 1)"
                            >Closes soon</span
                          ><span style="font-weight: 400">
                            ⋅ 4 PM ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 602900</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3892;keydown:pane.wfvdle3892;mouseover:pane.wfvdle3892;mouseout:pane.wfvdle3892"
                aria-label="Visit Directorate General for Growth, Ministry of Finance's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJOVFJb0FBIiwiLEFPdlZhdzJOOU5paE5SajNnN3Jvb2JCVThNck8sLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0loUU1vRHcsIl0="
                href="http://www.dgepcd.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3893;keydown:pane.wfvdle3893;mouseover:pane.wfvdle3893;mouseout:pane.wfvdle3893"
                aria-label="Get directions to Directorate General for Growth, Ministry of Finance"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJOVFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3894;mouseout:pane.wfvdle3894"
    >
      <a
        class="hfpxzc"
        aria-label="Başbakanlık Denetleme Kurumu"
        href="https://www.google.com/maps/place/Ba%C5%9Fbakanl%C4%B1k+Denetleme+Kurumu/data=!4m7!3m6!1s0x14de1737c8f06d4f:0x6513b5227b51a7eb!8m2!3d35.184477!4d33.357604!16s%2Fg%2F11b7q86ps4!19sChIJT23wyDcX3hQR66dReyK1E2U?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3894;focus:pane.wfvdle3894;blur:pane.wfvdle3894;auxclick:pane.wfvdle3894;keydown:pane.wfvdle3894;clickmod:pane.wfvdle3894"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbUFNb0FBIixudWxsLDU2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Başbakanlık Denetleme Kurumu
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3896;keydown:pane.wfvdle3896;mouseover:pane.wfvdle3896;mouseout:pane.wfvdle3896"
                aria-label="Get directions to Başbakanlık Denetleme Kurumu"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJbUFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3897;mouseout:pane.wfvdle3897"
    >
      <a
        class="hfpxzc"
        aria-label="General Embassy of Greece"
        href="https://www.google.com/maps/place/General+Embassy+of+Greece/data=!4m7!3m6!1s0x14de17d74616d5d7:0xc55ff26f6dfaabe2!8m2!3d35.1697431!4d33.353993!16s%2Fg%2F11ssdqdf9s!19sChIJ19UWRtcX3hQR4qv6bW_yX8U?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3897;focus:pane.wfvdle3897;blur:pane.wfvdle3897;auxclick:pane.wfvdle3897;keydown:pane.wfvdle3897;clickmod:pane.wfvdle3897"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJcUFNb0FBIixudWxsLDU3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      General Embassy of Greece
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.0 stars 4 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(4)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5993+VHX</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3899;keydown:pane.wfvdle3899;mouseover:pane.wfvdle3899;mouseout:pane.wfvdle3899"
                aria-label="Get directions to General Embassy of Greece"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJcUFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3900;mouseout:pane.wfvdle3900"
    >
      <a
        class="hfpxzc"
        aria-label="Statistical Service of Cyprus"
        href="https://www.google.com/maps/place/Statistical+Service+of+Cyprus/data=!4m7!3m6!1s0x14de17d623d570e1:0x7fd6d03073b89730!8m2!3d35.1670775!4d33.3543309!16s%2Fg%2F11q1jrctbx!19sChIJ4XDVI9YX3hQRMJe4czDQ1n8?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3900;focus:pane.wfvdle3900;blur:pane.wfvdle3900;auxclick:pane.wfvdle3900;keydown:pane.wfvdle3900;clickmod:pane.wfvdle3900"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJdmdNb0FBIixudWxsLDU4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Statistical Service of Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5983+RPP</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 602129</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3902;keydown:pane.wfvdle3902;mouseover:pane.wfvdle3902;mouseout:pane.wfvdle3902"
                aria-label="Get directions to Statistical Service of Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJdmdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3903;mouseout:pane.wfvdle3903"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of Energy"
        href="https://www.google.com/maps/place/Ministry+of+Energy/data=!4m7!3m6!1s0x14de190068dd3a45:0xa3512903b1faaa15!8m2!3d35.1599086!4d33.3637135!16s%2Fg%2F11y41dsm7t!19sChIJRTrdaAAZ3hQRFar6sQMpUaM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3903;focus:pane.wfvdle3903;blur:pane.wfvdle3903;auxclick:pane.wfvdle3903;keydown:pane.wfvdle3903;clickmod:pane.wfvdle3903"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJMWdNb0FBIixudWxsLDU5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of Energy
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5957+XF8, Andrea Araouzou</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3905;keydown:pane.wfvdle3905;mouseover:pane.wfvdle3905;mouseout:pane.wfvdle3905"
                aria-label="Get directions to Ministry of Energy"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJMWdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3906;mouseout:pane.wfvdle3906"
    >
      <a
        class="hfpxzc"
        aria-label="LTB Dayanışma ve Eğitim Merkezi"
        href="https://www.google.com/maps/place/LTB+Dayan%C4%B1%C5%9Fma+ve+E%C4%9Fitim+Merkezi/data=!4m7!3m6!1s0x14de17c90475d65b:0xdab892dabb84413c!8m2!3d35.1873815!4d33.3598076!16s%2Fg%2F11lkd97c1r!19sChIJW9Z1BMkX3hQRPEGEu9qSuNo?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3906;focus:pane.wfvdle3906;blur:pane.wfvdle3906;auxclick:pane.wfvdle3906;keydown:pane.wfvdle3906;clickmod:pane.wfvdle3906"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJN0FNb0FBIixudWxsLDYwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      LTB Dayanışma ve Eğitim Merkezi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Municipal office education</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Belediye Sk No 4</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 548 853 05 82</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3908;keydown:pane.wfvdle3908;mouseover:pane.wfvdle3908;mouseout:pane.wfvdle3908"
                aria-label="Visit LTB Dayanışma ve Eğitim Merkezi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJN0FNb0FBIiwiLEFPdlZhdzNqNV9aOTNiOC16VDN3NW4yS25WMGosLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0ktUU1vREEsIl0="
                href="http://www.lefkosabelediyesi.org/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3909;keydown:pane.wfvdle3909;mouseover:pane.wfvdle3909;mouseout:pane.wfvdle3909"
                aria-label="Get directions to LTB Dayanışma ve Eğitim Merkezi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJN0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3910;mouseout:pane.wfvdle3910"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Veteriner Dairesi"
        href="https://www.google.com/maps/place/KKTC+Veteriner+Dairesi/data=!4m7!3m6!1s0x14de16db4d1b1305:0x1995347190da18f9!8m2!3d35.2107334!4d33.3622676!16s%2Fg%2F11dx8p20vs!19sChIJBRMbTdsW3hQR-RjakHE0lRk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3910;focus:pane.wfvdle3910;blur:pane.wfvdle3910;auxclick:pane.wfvdle3910;keydown:pane.wfvdle3910;clickmod:pane.wfvdle3910"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJamdRb0FBIixudWxsLDYxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Veteriner Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.4 stars 30 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.4</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(30)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Veteriner Dairesi, Dr. Fazıl Küçük Bulvarı</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 225 35 51</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3912;keydown:pane.wfvdle3912;mouseover:pane.wfvdle3912;mouseout:pane.wfvdle3912"
                aria-label="Visit KKTC Veteriner Dairesi's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJamdRb0FBIiwiLEFPdlZhdzIyQVI2UmZaWXFQZzg3TEQ1YUNyWngsLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0lud1FvRHcsIl0="
                href="http://www.veteriner.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3913;keydown:pane.wfvdle3913;mouseover:pane.wfvdle3913;mouseout:pane.wfvdle3913"
                aria-label="Get directions to KKTC Veteriner Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJamdRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3914;mouseout:pane.wfvdle3914"
    >
      <a
        class="hfpxzc"
        aria-label="Δήμος Κυθρέας"
        href="https://www.google.com/maps/place/%CE%94%CE%AE%CE%BC%CE%BF%CF%82+%CE%9A%CF%85%CE%B8%CF%81%CE%AD%CE%B1%CF%82/data=!4m7!3m6!1s0x14de1702aa2ede6f:0x94b5402fbf46e25f!8m2!3d35.1750796!4d33.369786!16s%2Fg%2F11fmrq9265!19sChIJb94uqgIX3hQRX-JGvy9AtZQ?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3914;focus:pane.wfvdle3914;blur:pane.wfvdle3914;auxclick:pane.wfvdle3914;keydown:pane.wfvdle3914;clickmod:pane.wfvdle3914"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJc3dRb0FBIixudWxsLDYyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Δήμος Κυθρέας</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City Hall</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Ammochostou 37-1016</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 438956</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3916;keydown:pane.wfvdle3916;mouseover:pane.wfvdle3916;mouseout:pane.wfvdle3916"
                aria-label="Visit Δήμος Κυθρέας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJc3dRb0FBIiwiLEFPdlZhdzNRS1ZtVThOdFBWTVZFY3d1cW9CU2QsLDBhaFVLRXdpTjU4enN4WUNHQXhYbEF0c0VIZUtvQ0FVUTYxZ0l3d1FvRHcsIl0="
                href="http://www.kythrea.com/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3917;keydown:pane.wfvdle3917;mouseover:pane.wfvdle3917;mouseout:pane.wfvdle3917"
                aria-label="Get directions to Δήμος Κυθρέας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aU41OHpzeFlDR0F4WGxBdHNFSGVLb0NBVVE4QmNJc3dRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3918;mouseout:pane.wfvdle3918"
    >
      <a
        class="hfpxzc"
        aria-label="Κτίριο Αρχιγραμματείας"
        href="https://www.google.com/maps/place/%CE%9A%CF%84%CE%AF%CF%81%CE%B9%CE%BF+%CE%91%CF%81%CF%87%CE%B9%CE%B3%CF%81%CE%B1%CE%BC%CE%BC%CE%B1%CF%84%CE%B5%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de170032b307c1:0x62a7e3ff6273410e!8m2!3d35.1660883!4d33.3546063!16s%2Fg%2F11vyydxfx3!19sChIJwQezMgAX3hQRDkFzYv_jp2I?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3918;focus:pane.wfvdle3918;blur:pane.wfvdle3918;auxclick:pane.wfvdle3918;keydown:pane.wfvdle3918;clickmod:pane.wfvdle3918"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJQlNnQSIsbnVsbCw2NF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Κτίριο Αρχιγραμματείας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5983+CRQ, Dimostheni Severi</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3920;keydown:pane.wfvdle3920;mouseover:pane.wfvdle3920;mouseout:pane.wfvdle3920"
                aria-label="Get directions to Κτίριο Αρχιγραμματείας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3921;mouseout:pane.wfvdle3921"
    >
      <a
        class="hfpxzc"
        aria-label="Office of the Commissioner for the Environment of the Republic of Cyprus"
        href="https://www.google.com/maps/place/Office+of+the+Commissioner+for+the+Environment+of+the+Republic+of+Cyprus/data=!4m7!3m6!1s0x14de1986ea6fab5b:0x470d051306cd0eaf!8m2!3d35.1566727!4d33.3520177!16s%2Fg%2F11hf4qs2zg!19sChIJW6tv6oYZ3hQRrw7NBhMFDUc?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3921;focus:pane.wfvdle3921;blur:pane.wfvdle3921;auxclick:pane.wfvdle3921;keydown:pane.wfvdle3921;clickmod:pane.wfvdle3921"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJR3lnQSIsbnVsbCw2NV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Office of the Commissioner for the Environment of the
                      Republic of Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Environment office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Kyriakou Matsi 56</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 96 600219</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3923;keydown:pane.wfvdle3923;mouseover:pane.wfvdle3923;mouseout:pane.wfvdle3923"
                aria-label="Get directions to Office of the Commissioner for the Environment of the Republic of Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJR3lnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3924;mouseout:pane.wfvdle3924"
    >
      <a
        class="hfpxzc"
        aria-label="Kktc Ekonomi Ve Enerji Bakanlığı"
        href="https://www.google.com/maps/place/Kktc+Ekonomi+Ve+Enerji+Bakanl%C4%B1%C4%9F%C4%B1/data=!4m7!3m6!1s0x14de1732b4ae9def:0x3b77ce9d31f15f90!8m2!3d35.1950481!4d33.3484276!16s%2Fg%2F11b7q87kw_!19sChIJ752utDIX3hQRkF_xMZ3Odzs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3924;focus:pane.wfvdle3924;blur:pane.wfvdle3924;auxclick:pane.wfvdle3924;keydown:pane.wfvdle3924;clickmod:pane.wfvdle3924"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJTXlnQSIsbnVsbCw2Nl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kktc Ekonomi Ve Enerji Bakanlığı
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.6 stars 5 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.6</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(5)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Selçuklu Cd</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 33 41</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3926;keydown:pane.wfvdle3926;mouseover:pane.wfvdle3926;mouseout:pane.wfvdle3926"
                aria-label="Get directions to Kktc Ekonomi Ve Enerji Bakanlığı"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJTXlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3927;mouseout:pane.wfvdle3927"
    >
      <a
        class="hfpxzc"
        aria-label="Ένωση Δήμων Κύπρου"
        href="https://www.google.com/maps/place/%CE%88%CE%BD%CF%89%CF%83%CE%B7+%CE%94%CE%AE%CE%BC%CF%89%CE%BD+%CE%9A%CF%8D%CF%80%CF%81%CE%BF%CF%85/data=!4m7!3m6!1s0x14de175046ebe757:0x9933d147c64e493c!8m2!3d35.1721333!4d33.3580327!16s%2Fg%2F1hg5132tl!19sChIJV-frRlAX3hQRPElOxkfRM5k?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3927;focus:pane.wfvdle3927;blur:pane.wfvdle3927;auxclick:pane.wfvdle3927;keydown:pane.wfvdle3927;clickmod:pane.wfvdle3927"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJU2lnQSIsbnVsbCw2N10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ένωση Δήμων Κύπρου
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Rigenis 78</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 445170</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3929;keydown:pane.wfvdle3929;mouseover:pane.wfvdle3929;mouseout:pane.wfvdle3929"
                aria-label="Visit Ένωση Δήμων Κύπρου's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJU2lnQSIsIixBT3ZWYXczT2lWNlBRbHJ1dnpvYkdvVEJZajBrLCwwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E2MWdJV2lnUCwiXQ=="
                href="http://www.ucm.org.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3930;keydown:pane.wfvdle3930;mouseover:pane.wfvdle3930;mouseout:pane.wfvdle3930"
                aria-label="Get directions to Ένωση Δήμων Κύπρου"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJU2lnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3931;mouseout:pane.wfvdle3931"
    >
      <a
        class="hfpxzc"
        aria-label="Επιτροπή Εκπαιδευτικής Υπηρεσίας"
        href="https://www.google.com/maps/place/%CE%95%CF%80%CE%B9%CF%84%CF%81%CE%BF%CF%80%CE%AE+%CE%95%CE%BA%CF%80%CE%B1%CE%B9%CE%B4%CE%B5%CF%85%CF%84%CE%B9%CE%BA%CE%AE%CF%82+%CE%A5%CF%80%CE%B7%CF%81%CE%B5%CF%83%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de17f3752c4877:0xddf328d3d439176b!8m2!3d35.1669418!4d33.3538545!16s%2Fg%2F11h7dtgk5g!19sChIJd0gsdfMX3hQRaxc51NMo890?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3931;focus:pane.wfvdle3931;blur:pane.wfvdle3931;auxclick:pane.wfvdle3931;keydown:pane.wfvdle3931;clickmod:pane.wfvdle3931"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJWmlnQSIsbnVsbCw2OF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Επιτροπή Εκπαιδευτικής Υπηρεσίας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.3 stars 12 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.3</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(12)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Michalaki Karaoli</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 602660</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3933;keydown:pane.wfvdle3933;mouseover:pane.wfvdle3933;mouseout:pane.wfvdle3933"
                aria-label="Visit Επιτροπή Εκπαιδευτικής Υπηρεσίας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJWmlnQSIsIixBT3ZWYXcxUDhVX2w0cmYxM2RlYUIzU0lnT25hLCwwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E2MWdJZUNnUSwiXQ=="
                href="http://www.eey.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3934;keydown:pane.wfvdle3934;mouseover:pane.wfvdle3934;mouseout:pane.wfvdle3934"
                aria-label="Get directions to Επιτροπή Εκπαιδευτικής Υπηρεσίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJWmlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3935;mouseout:pane.wfvdle3935"
    >
      <a
        class="hfpxzc"
        aria-label="Cyprus Public Audit Oversight Board CyPAOB"
        href="https://www.google.com/maps/place/Cyprus+Public+Audit+Oversight+Board+CyPAOB/data=!4m7!3m6!1s0x14de179c947a4a19:0x52734a80438cdfbd!8m2!3d35.1627198!4d33.3653678!16s%2Fg%2F11l7468r_z!19sChIJGUp6lJwX3hQRvd-MQ4BKc1I?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3935;focus:pane.wfvdle3935;blur:pane.wfvdle3935;auxclick:pane.wfvdle3935;keydown:pane.wfvdle3935;clickmod:pane.wfvdle3935"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJalFFb0FBIixudWxsLDY5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Cyprus Public Audit Oversight Board CyPAOB
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Dimofontos 1</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3937;keydown:pane.wfvdle3937;mouseover:pane.wfvdle3937;mouseout:pane.wfvdle3937"
                aria-label="Get directions to Cyprus Public Audit Oversight Board CyPAOB"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJalFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3938;mouseout:pane.wfvdle3938"
    >
      <a
        class="hfpxzc"
        aria-label="KKTC Yüksek Mahkeme Supreme Court - Lefkoşa Kaza Mahkemesi"
        href="https://www.google.com/maps/place/KKTC+Y%C3%BCksek+Mahkeme+Supreme+Court+-+Lefko%C5%9Fa+Kaza+Mahkemesi/data=!4m7!3m6!1s0x14de17461ce4ba0d:0xfc6b7ede2d335e66!8m2!3d35.1785201!4d33.3600376!16s%2Fg%2F11f5dg5fg8!19sChIJDbrkHEYX3hQRZl4zLd5-a_w?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3938;focus:pane.wfvdle3938;blur:pane.wfvdle3938;auxclick:pane.wfvdle3938;keydown:pane.wfvdle3938;clickmod:pane.wfvdle3938"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJb1FFb0FBIixudWxsLDcwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      KKTC Yüksek Mahkeme Supreme Court - Lefkoşa Kaza Mahkemesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.2 stars 6 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.2</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(6)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City courthouse</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Sarayönü Sokak, Opposite Post, Lefkoşa</span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3941;keydown:pane.wfvdle3941;mouseover:pane.wfvdle3941;mouseout:pane.wfvdle3941"
                aria-label="Get directions to KKTC Yüksek Mahkeme Supreme Court - Lefkoşa Kaza Mahkemesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJb1FFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue">
          <div class="AyRUI" role="presentation" style="height: 8px">
            &nbsp;
          </div>
          <div class="n8sPKe ccePVe">
            <div class="Ahnjwc fontBodyMedium">
              <div class="W6VQef">
                <div
                  aria-hidden="true"
                  class="JoXfOb fCbqBc"
                  style="width: 16px; height: 16px"
                >
                  <img
                    alt=""
                    class="Jn12ke xcEj5d"
                    src="https://ssl.gstatic.com/local/servicebusiness/default_user.png"
                    style="width: 16px; height: 16px"
                  />
                </div>
                <div class="ah5Ghc">
                  <span style="font-weight: 400"
                    >"I stumbled across this interesting building next to
                    Ataturk Square,&nbsp;..."</span
                  >
                </div>
              </div>
              <div class="Q4BGF"></div>
            </div>
          </div>
        </div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3942;mouseout:pane.wfvdle3942"
    >
      <a
        class="hfpxzc"
        aria-label="Lympia"
        href="https://www.google.com/maps/place/Lympia/data=!4m7!3m6!1s0x14de114dd4a2812f:0x794ff0f52fa44dff!8m2!3d35.1715328!4d33.3485709!16s%2Fg%2F11ty2vdlsd!19sChIJL4Gi1E0R3hQR_02kL_XwT3k?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3942;focus:pane.wfvdle3942;blur:pane.wfvdle3942;auxclick:pane.wfvdle3942;keydown:pane.wfvdle3942;clickmod:pane.wfvdle3942"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJdHdFb0FBIixudWxsLDcxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Lympia</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Ilioupoleos 12</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3944;keydown:pane.wfvdle3944;mouseover:pane.wfvdle3944;mouseout:pane.wfvdle3944"
                aria-label="Get directions to Lympia"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJdHdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3945;mouseout:pane.wfvdle3945"
    >
      <a
        class="hfpxzc"
        aria-label="Phillipine Consulate"
        href="https://www.google.com/maps/place/Phillipine+Consulate/data=!4m7!3m6!1s0x14de170e75059ff7:0xc2190c60a9246f78!8m2!3d35.1659611!4d33.3604319!16s%2Fg%2F11r35h243p!19sChIJ958FdQ4X3hQReG8kqWAMGcI?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3945;focus:pane.wfvdle3945;blur:pane.wfvdle3945;auxclick:pane.wfvdle3945;keydown:pane.wfvdle3945;clickmod:pane.wfvdle3945"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJeXdFb0FBIixudWxsLDcyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Phillipine Consulate
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Council</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Stasikratous 16-7th Floor</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3947;keydown:pane.wfvdle3947;mouseover:pane.wfvdle3947;mouseout:pane.wfvdle3947"
                aria-label="Get directions to Phillipine Consulate"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJeXdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3948;mouseout:pane.wfvdle3948"
    >
      <a
        class="hfpxzc"
        aria-label="Ahmet Savaşan"
        href="https://www.google.com/maps/place/Ahmet+Sava%C5%9Fan/data=!4m7!3m6!1s0x14de1748be693ca9:0x3d0a028e6664a117!8m2!3d35.1793268!4d33.3587147!16s%2Fg%2F11tjhkjnrf!19sChIJqTxpvkgX3hQRF6FkZo4CCj0?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3948;focus:pane.wfvdle3948;blur:pane.wfvdle3948;auxclick:pane.wfvdle3948;keydown:pane.wfvdle3948;clickmod:pane.wfvdle3948"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJNGdFb0FBIixudWxsLDczXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Ahmet Savaşan</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Pencizade Sk 11</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 548 858 99 99</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3950;keydown:pane.wfvdle3950;mouseover:pane.wfvdle3950;mouseout:pane.wfvdle3950"
                aria-label="Visit Ahmet Savaşan's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJNGdFb0FBIiwiLEFPdlZhdzBiMnZ2TzdBZ1dzYnJWcTVhNnF1T1EsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0k3d0VvREEsIl0="
                href="http://ahmetsavasan.biz/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3951;keydown:pane.wfvdle3951;mouseover:pane.wfvdle3951;mouseout:pane.wfvdle3951"
                aria-label="Get directions to Ahmet Savaşan"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJNGdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3952;mouseout:pane.wfvdle3952"
    >
      <a
        class="hfpxzc"
        aria-label="Cyprus Foundations Administration EVKAF"
        href="https://www.google.com/maps/place/Cyprus+Foundations+Administration+EVKAF/data=!4m7!3m6!1s0x14de1745e5210b67:0xaa95e746b63ed2e2!8m2!3d35.1770863!4d33.3607806!16s%2Fg%2F1tcyznc6!19sChIJZwsh5UUX3hQR4tI-tkbnlao?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3952;focus:pane.wfvdle3952;blur:pane.wfvdle3952;auxclick:pane.wfvdle3952;keydown:pane.wfvdle3952;clickmod:pane.wfvdle3952"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJLUFFb0FBIixudWxsLDc0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Cyprus Foundations Administration EVKAF
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.4 stars 25 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.4</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(25)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Foundation</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Girne Cd</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5:30 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 228 31 34</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3954;keydown:pane.wfvdle3954;mouseover:pane.wfvdle3954;mouseout:pane.wfvdle3954"
                aria-label="Visit Cyprus Foundations Administration EVKAF's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJLUFFb0FBIiwiLEFPdlZhdzByeG5SdW9ZNENxY2JPb1o5R0JOX2YsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0lod0lvRFEsIl0="
                href="http://www.evkaf.org/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3955;keydown:pane.wfvdle3955;mouseover:pane.wfvdle3955;mouseout:pane.wfvdle3955"
                aria-label="Get directions to Cyprus Foundations Administration EVKAF"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJLUFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3956;mouseout:pane.wfvdle3956"
    >
      <a
        class="hfpxzc"
        aria-label="Nicosia Town Hall"
        href="https://www.google.com/maps/place/Nicosia+Town+Hall/data=!4m7!3m6!1s0x14de1771367776a5:0xfc97383a50cb6fb7!8m2!3d35.1736632!4d33.3656704!16s%2Fg%2F11s47cr_g1!19sChIJpXZ3NnEX3hQRt2_LUDo4l_w?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3956;focus:pane.wfvdle3956;blur:pane.wfvdle3956;auxclick:pane.wfvdle3956;keydown:pane.wfvdle3956;clickmod:pane.wfvdle3956"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJblFJb0FBIixudWxsLDc1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Nicosia Town Hall
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Eptanisou 11-1016</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3958;keydown:pane.wfvdle3958;mouseover:pane.wfvdle3958;mouseout:pane.wfvdle3958"
                aria-label="Visit Nicosia Town Hall's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJblFJb0FBIiwiLEFPdlZhdzIwMWYtcVVMeGt6dWhWb0toU0s4UFgsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0lxd0lvREEsIl0="
                href="https://www.nicosia.org.cy/el-GR/home/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3959;keydown:pane.wfvdle3959;mouseover:pane.wfvdle3959;mouseout:pane.wfvdle3959"
                aria-label="Get directions to Nicosia Town Hall"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJblFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3960;mouseout:pane.wfvdle3960"
    >
      <a
        class="hfpxzc"
        aria-label="Υπηρεσία Προστασίας Καταναλωτή"
        href="https://www.google.com/maps/place/%CE%A5%CF%80%CE%B7%CF%81%CE%B5%CF%83%CE%AF%CE%B1+%CE%A0%CF%81%CE%BF%CF%83%CF%84%CE%B1%CF%83%CE%AF%CE%B1%CF%82+%CE%9A%CE%B1%CF%84%CE%B1%CE%BD%CE%B1%CE%BB%CF%89%CF%84%CE%AE/data=!4m7!3m6!1s0x14de175f4ae327ab:0x53ebec72feed5e8c!8m2!3d35.161891!4d33.364938!16s%2Fg%2F11c30y00ny!19sChIJqyfjSl8X3hQRjF7t_nLs61M?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3960;focus:pane.wfvdle3960;blur:pane.wfvdle3960;auxclick:pane.wfvdle3960;keydown:pane.wfvdle3960;clickmod:pane.wfvdle3960"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJd1FJb0FBIixudWxsLDc2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Υπηρεσία Προστασίας Καταναλωτή
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Agapinoros 2</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 817040</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3962;keydown:pane.wfvdle3962;mouseover:pane.wfvdle3962;mouseout:pane.wfvdle3962"
                aria-label="Visit Υπηρεσία Προστασίας Καταναλωτή's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJd1FJb0FBIiwiLEFPdlZhdzN4akJLWGpqcjBzRGUwR2N5eVFfNDAsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0kwd0lvRUEsIl0="
                href="http://www.consumer.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3963;keydown:pane.wfvdle3963;mouseover:pane.wfvdle3963;mouseout:pane.wfvdle3963"
                aria-label="Get directions to Υπηρεσία Προστασίας Καταναλωτή"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJd1FJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3964;mouseout:pane.wfvdle3964"
    >
      <a
        class="hfpxzc"
        aria-label="Τμήμα Γεωδεσίας"
        href="https://www.google.com/maps/place/%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%93%CE%B5%CF%89%CE%B4%CE%B5%CF%83%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de19e295c1191b:0xf2c9bd5d5b9c763b!8m2!3d35.1617401!4d33.3613425!16s%2Fg%2F12qfj81l8!19sChIJGxnBleIZ3hQRO3acW129yfI?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3964;focus:pane.wfvdle3964;blur:pane.wfvdle3964;auxclick:pane.wfvdle3964;keydown:pane.wfvdle3964;clickmod:pane.wfvdle3964"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJNkFJb0FBIixudWxsLDc3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Τμήμα Γεωδεσίας</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5966+MGW, Chytron</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3966;keydown:pane.wfvdle3966;mouseover:pane.wfvdle3966;mouseout:pane.wfvdle3966"
                aria-label="Get directions to Τμήμα Γεωδεσίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJNkFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3967;mouseout:pane.wfvdle3967"
    >
      <a
        class="hfpxzc"
        aria-label="Treasury of the Republic of Cyprus"
        href="https://www.google.com/maps/place/Treasury+of+the+Republic+of+Cyprus/data=!4m7!3m6!1s0x14de1792e3779cc3:0x9c3c23a1ee948778!8m2!3d35.1672817!4d33.3544526!16s%2Fg%2F11jk4_cjr6!19sChIJw5x345IX3hQReIeU7qEjPJw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3967;focus:pane.wfvdle3967;blur:pane.wfvdle3967;auxclick:pane.wfvdle3967;keydown:pane.wfvdle3967;clickmod:pane.wfvdle3967"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJX2dJb0FBIixudWxsLDc4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Treasury of the Republic of Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.0 stars 16 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(16)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >M.Karaoli &amp; Gr. Afxentiou str Nicosia</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 602310</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3969;keydown:pane.wfvdle3969;mouseover:pane.wfvdle3969;mouseout:pane.wfvdle3969"
                aria-label="Visit Treasury of the Republic of Cyprus's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJX2dJb0FBIiwiLEFPdlZhdzBDZENXM3M4ZzE0TW5BVHlIOWVoZ2YsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0lqd01vRHcsIl0="
                href="http://www.treasury.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3970;keydown:pane.wfvdle3970;mouseover:pane.wfvdle3970;mouseout:pane.wfvdle3970"
                aria-label="Get directions to Treasury of the Republic of Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJX2dJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3971;mouseout:pane.wfvdle3971"
    >
      <a
        class="hfpxzc"
        aria-label="YAGA - Kıbrıs Türk Yatırım Geliştirme Ajansı (Cyprus Turkish Investment Development Agency)"
        href="https://www.google.com/maps/place/YAGA+-+K%C4%B1br%C4%B1s+T%C3%BCrk+Yat%C4%B1r%C4%B1m+Geli%C5%9Ftirme+Ajans%C4%B1+%28Cyprus+Turkish+Investment+Development+Agency%29/data=!4m7!3m6!1s0x14de17f18a4b78af:0x3831c5162ad29780!8m2!3d35.1831617!4d33.3532521!16s%2Fg%2F11l2byktxp!19sChIJr3hLivEX3hQRgJfSKhbFMTg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3971;focus:pane.wfvdle3971;blur:pane.wfvdle3971;auxclick:pane.wfvdle3971;keydown:pane.wfvdle3971;clickmod:pane.wfvdle3971"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJb1FNb0FBIixudWxsLDc5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      YAGA - Kıbrıs Türk Yatırım Geliştirme Ajansı (Cyprus
                      Turkish Investment Development Agency)
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Tabak Derviş Sk 5</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 228 23 17</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3973;keydown:pane.wfvdle3973;mouseover:pane.wfvdle3973;mouseout:pane.wfvdle3973"
                aria-label="Visit YAGA - Kıbrıs Türk Yatırım Geliştirme Ajansı (Cyprus Turkish Investment Development Agency)'s website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJb1FNb0FBIiwiLEFPdlZhdzBVMzEzVS1BZ1l0RC1lMGdNQXBEd3MsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0lyZ01vREEsIl0="
                href="https://www.yaga.gov.ct.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3974;keydown:pane.wfvdle3974;mouseover:pane.wfvdle3974;mouseout:pane.wfvdle3974"
                aria-label="Get directions to YAGA - Kıbrıs Türk Yatırım Geliştirme Ajansı (Cyprus Turkish Investment Development Agency)"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJb1FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3975;mouseout:pane.wfvdle3975"
    >
      <a
        class="hfpxzc"
        aria-label="Embassy of Turkey"
        href="https://www.google.com/maps/place/Embassy+of+Turkey/data=!4m7!3m6!1s0x14de17480213170b:0xca10a3595263b858!8m2!3d35.1834487!4d33.3592185!16s%2Fm%2F02855fy!19sChIJCxcTAkgX3hQRWLhjUlmjEMo?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3975;focus:pane.wfvdle3975;blur:pane.wfvdle3975;auxclick:pane.wfvdle3975;keydown:pane.wfvdle3975;clickmod:pane.wfvdle3975"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJdVFNb0FBIixudWxsLDgwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Embassy of Turkey
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.8 stars 411 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.8</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(411)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Embassy</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59M5+9MG</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 6 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 600 31 00</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3977;keydown:pane.wfvdle3977;mouseover:pane.wfvdle3977;mouseout:pane.wfvdle3977"
                aria-label="Visit Embassy of Turkey's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJdVFNb0FBIiwiLEFPdlZhdzFEaHZrWEF3d2I1OUk1SGN3Um5BaWIsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0l5QU1vRFEsIl0="
                href="http://nicosia.emb.mfa.gov.tr/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3978;keydown:pane.wfvdle3978;mouseover:pane.wfvdle3978;mouseout:pane.wfvdle3978"
                aria-label="Get directions to Embassy of Turkey"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJdVFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3979;mouseout:pane.wfvdle3979"
    >
      <a
        class="hfpxzc"
        aria-label="Department of Insolvency - Τμήμα Αφερεγγυότητας"
        href="https://www.google.com/maps/place/Department+of+Insolvency+-+%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%91%CF%86%CE%B5%CF%81%CE%B5%CE%B3%CE%B3%CF%85%CF%8C%CF%84%CE%B7%CF%84%CE%B1%CF%82/data=!4m7!3m6!1s0x14de175876a552e5:0x218583c8e630d9b9!8m2!3d35.1628236!4d33.3615858!16s%2Fg%2F11dztrfymz!19sChIJ5VKldlgX3hQRudkw5siDhSE?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3979;focus:pane.wfvdle3979;blur:pane.wfvdle3979;auxclick:pane.wfvdle3979;keydown:pane.wfvdle3979;clickmod:pane.wfvdle3979"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJM2dNb0FBIixudWxsLDgxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Department of Insolvency - Τμήμα Αφερεγγυότητας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Gerasimou Markora &amp;, Andrea Michalakopoulou
                          19</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 466510</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3981;keydown:pane.wfvdle3981;mouseover:pane.wfvdle3981;mouseout:pane.wfvdle3981"
                aria-label="Visit Department of Insolvency - Τμήμα Αφερεγγυότητας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJM2dNb0FBIiwiLEFPdlZhdzNadFJ6XzgwQmtkOGtTcmt0Qk52c2ksLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0k4QU1vRVEsIl0="
                href="http://www.insolvency.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3982;keydown:pane.wfvdle3982;mouseover:pane.wfvdle3982;mouseout:pane.wfvdle3982"
                aria-label="Get directions to Department of Insolvency - Τμήμα Αφερεγγυότητας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJM2dNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3983;mouseout:pane.wfvdle3983"
    >
      <a
        class="hfpxzc"
        aria-label="Civil Registry and Migration Department"
        href="https://www.google.com/maps/place/Civil+Registry+and+Migration+Department/data=!4m7!3m6!1s0x14de17539177337d:0xc952ddf77c679f15!8m2!3d35.1603699!4d33.3709925!16s%2Fg%2F119wjzd26!19sChIJfTN3kVMX3hQRFZ9nfPfdUsk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3983;focus:pane.wfvdle3983;blur:pane.wfvdle3983;auxclick:pane.wfvdle3983;keydown:pane.wfvdle3983;clickmod:pane.wfvdle3983"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJaFFRb0FBIixudWxsLDgyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Civil Registry and Migration Department
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.2 stars 249 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.2</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(249)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span
                        ><span
                          >Immigration &amp; naturalization service</span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Λεωφ. Αρχιεπισκόπου Μακαρίου Γ' 90</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 308808</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3986;keydown:pane.wfvdle3986;mouseover:pane.wfvdle3986;mouseout:pane.wfvdle3986"
                aria-label="Visit Civil Registry and Migration Department's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJaFFRb0FBIiwiLEFPdlZhdzE5a0FaMzM0bWh1Q1VpdGpWMnpoaVcsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0lsZ1FvRHcsIl0="
                href="http://www.moi.gov.cy/crmd"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3987;keydown:pane.wfvdle3987;mouseover:pane.wfvdle3987;mouseout:pane.wfvdle3987"
                aria-label="Get directions to Civil Registry and Migration Department"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJaFFRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue">
          <div class="AyRUI" role="presentation" style="height: 8px">
            &nbsp;
          </div>
          <div class="n8sPKe ccePVe">
            <div class="Ahnjwc fontBodyMedium">
              <div class="W6VQef">
                <div
                  aria-hidden="true"
                  class="JoXfOb fCbqBc"
                  style="width: 16px; height: 16px"
                >
                  <img
                    alt=""
                    class="Jn12ke xcEj5d"
                    src="https://ssl.gstatic.com/local/servicebusiness/default_user.png"
                    style="width: 16px; height: 16px"
                  />
                </div>
                <div class="ah5Ghc">
                  <span style="font-weight: 400">"Nice </span
                  ><span style="font-weight: 500">government</span
                  ><span style="font-weight: 400">
                    clerk. As long as you documents meets Cyprus&nbsp;..."</span
                  >
                </div>
              </div>
              <div class="Q4BGF"></div>
            </div>
          </div>
        </div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3988;mouseout:pane.wfvdle3988"
    >
      <a
        class="hfpxzc"
        aria-label="European Commission in Cyprus"
        href="https://www.google.com/maps/place/European+Commission+in+Cyprus/data=!4m7!3m6!1s0x14de1755b77f3bf5:0x5499d60159dee070!8m2!3d35.1672689!4d33.3526406!16s%2Fg%2F11hblhj39p!19sChIJ9Tt_t1UX3hQRcODeWQHWmVQ?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3988;focus:pane.wfvdle3988;blur:pane.wfvdle3988;auxclick:pane.wfvdle3988;keydown:pane.wfvdle3988;clickmod:pane.wfvdle3988"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJckFRb0FBIixudWxsLDgzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      European Commission in Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.8 stars 6 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.8</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(6)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Lordou Vyronos 30</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 5 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 817770</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3990;keydown:pane.wfvdle3990;mouseover:pane.wfvdle3990;mouseout:pane.wfvdle3990"
                aria-label="Visit European Commission in Cyprus's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJckFRb0FBIiwiLEFPdlZhdzM2cW81cFhoazR5WVRTb2puWGE2NWcsLDBhaFVLRXdqMHM4ZnR4WUNHQXhXckF0c0VIYTduQjFnUTYxZ0l2Z1FvRUEsIl0="
                href="https://ec.europa.eu/cyprus/home_en"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3991;keydown:pane.wfvdle3991;mouseover:pane.wfvdle3991;mouseout:pane.wfvdle3991"
                aria-label="Get directions to European Commission in Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3ajBzOGZ0eFlDR0F4V3JBdHNFSGE3bkIxZ1E4QmNJckFRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3992;mouseout:pane.wfvdle3992"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of Labour and Social Insurance"
        href="https://www.google.com/maps/place/Ministry+of+Labour+and+Social+Insurance/data=!4m7!3m6!1s0x14de17542064b445:0xacc019df38c9e7da!8m2!3d35.1632502!4d33.3606425!16s%2Fg%2F1hf3s7j_q!19sChIJRbRkIFQX3hQR2ufJON8ZwKw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3992;focus:pane.wfvdle3992;blur:pane.wfvdle3992;auxclick:pane.wfvdle3992;keydown:pane.wfvdle3992;clickmod:pane.wfvdle3992"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJQlNnQSIsbnVsbCw4NV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of Labour and Social Insurance
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.7 stars 109 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(109)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Spyrou Kyprianou Avenue 26</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 401600</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle3994;keydown:pane.wfvdle3994;mouseover:pane.wfvdle3994;mouseout:pane.wfvdle3994"
                aria-label="Visit Ministry of Labour and Social Insurance's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJQlNnQSIsIixBT3ZWYXczSGJ4ZGQweW42dHF3YWxwdXZtanFtLCwwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE2MWdJRnlnUSwiXQ=="
                href="http://www.mlsi.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3995;keydown:pane.wfvdle3995;mouseover:pane.wfvdle3995;mouseout:pane.wfvdle3995"
                aria-label="Get directions to Ministry of Labour and Social Insurance"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle3996;mouseout:pane.wfvdle3996"
    >
      <a
        class="hfpxzc"
        aria-label="Γενική Διεύθυνση Ανάπτυξης, Υπουργείο Οικονομικών"
        href="https://www.google.com/maps/place/%CE%93%CE%B5%CE%BD%CE%B9%CE%BA%CE%AE+%CE%94%CE%B9%CE%B5%CF%8D%CE%B8%CF%85%CE%BD%CF%83%CE%B7+%CE%91%CE%BD%CE%AC%CF%80%CF%84%CF%85%CE%BE%CE%B7%CF%82,+%CE%A5%CF%80%CE%BF%CF%85%CF%81%CE%B3%CE%B5%CE%AF%CE%BF+%CE%9F%CE%B9%CE%BA%CE%BF%CE%BD%CE%BF%CE%BC%CE%B9%CE%BA%CF%8E%CE%BD/data=!4m7!3m6!1s0x14de1714dcbfb511:0xeded8609f9fffb12!8m2!3d35.1678813!4d33.3536284!16s%2Fg%2F11ss8bg8ml!19sChIJEbW_3BQX3hQREvv_-QmG7e0?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3996;focus:pane.wfvdle3996;blur:pane.wfvdle3996;auxclick:pane.wfvdle3996;keydown:pane.wfvdle3996;clickmod:pane.wfvdle3996"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJTFNnQSIsbnVsbCw4Nl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Γενική Διεύθυνση Ανάπτυξης, Υπουργείο Οικονομικών
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Λεωφόρος Βύρωνος 29-1096</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle3998;keydown:pane.wfvdle3998;mouseover:pane.wfvdle3998;mouseout:pane.wfvdle3998"
                aria-label="Get directions to Γενική Διεύθυνση Ανάπτυξης, Υπουργείο Οικονομικών"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJTFNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle3999;mouseout:pane.wfvdle3999"
    >
      <a
        class="hfpxzc"
        aria-label="Department of Antiquities, Republic of Cyprus"
        href="https://www.google.com/maps/place/Department+of+Antiquities,+Republic+of+Cyprus/data=!4m7!3m6!1s0x14de17b274f62fc5:0x46155cbd534f4dea!8m2!3d35.172061!4d33.3556413!16s%2Fg%2F11hm_dnbxs!19sChIJxS_2dLIX3hQR6k1PU71cFUY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle3999;focus:pane.wfvdle3999;blur:pane.wfvdle3999;auxclick:pane.wfvdle3999;keydown:pane.wfvdle3999;clickmod:pane.wfvdle3999"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJUUNnQSIsbnVsbCw4N10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Department of Antiquities, Republic of Cyprus
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59C4+R7C</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="font-weight: 400; color: rgba(176, 96, 0, 1)"
                            >Closes soon</span
                          ><span style="font-weight: 400">
                            ⋅ 4 PM ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 865888</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4001;keydown:pane.wfvdle4001;mouseover:pane.wfvdle4001;mouseout:pane.wfvdle4001"
                aria-label="Visit Department of Antiquities, Republic of Cyprus's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJUUNnQSIsIixBT3ZWYXczOGRXTG9Zenh4eGNZbDZuXzVMQWRDLCwwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE2MWdJVWlnUSwiXQ=="
                href="http://www.mcw.gov.cy/mcw/DA/DA.nsf/DMLindex_en/DMLindex_en?OpenDocument"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4002;keydown:pane.wfvdle4002;mouseover:pane.wfvdle4002;mouseout:pane.wfvdle4002"
                aria-label="Get directions to Department of Antiquities, Republic of Cyprus"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJUUNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4003;mouseout:pane.wfvdle4003"
    >
      <a
        class="hfpxzc"
        aria-label="Vergi Dairesi"
        href="https://www.google.com/maps/place/Vergi+Dairesi/data=!4m7!3m6!1s0x14de1737b89aaaab:0xfb3031b3749e7e7b!8m2!3d35.1845935!4d33.3579518!16s%2Fg%2F11kj908rqx!19sChIJq6qauDcX3hQRe36edLMxMPs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4003;focus:pane.wfvdle4003;blur:pane.wfvdle4003;auxclick:pane.wfvdle4003;keydown:pane.wfvdle4003;clickmod:pane.wfvdle4003"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJYUNnQSIsbnVsbCw4OF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Vergi Dairesi</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Tax department</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59M5+R5P, Ahmet Tansol Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4005;keydown:pane.wfvdle4005;mouseover:pane.wfvdle4005;mouseout:pane.wfvdle4005"
                aria-label="Get directions to Vergi Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJYUNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4006;mouseout:pane.wfvdle4006"
    >
      <a
        class="hfpxzc"
        aria-label="Nicosia Municipality Payment Offices"
        href="https://www.google.com/maps/place/Nicosia+Municipality+Payment+Offices/data=!4m7!3m6!1s0x14de17438531aec7:0x867b5aa8c7a7022e!8m2!3d35.1739955!4d33.3660073!16s%2Fg%2F11c6qc77q3!19sChIJx64xhUMX3hQRLgKnx6hae4Y?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4006;focus:pane.wfvdle4006;blur:pane.wfvdle4006;auxclick:pane.wfvdle4006;keydown:pane.wfvdle4006;clickmod:pane.wfvdle4006"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJZXlnQSIsbnVsbCw4OV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Nicosia Municipality Payment Offices
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City tax office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >13 Old Electric House building Street, Old 1016</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4008;keydown:pane.wfvdle4008;mouseover:pane.wfvdle4008;mouseout:pane.wfvdle4008"
                aria-label="Get directions to Nicosia Municipality Payment Offices"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJZXlnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4009;mouseout:pane.wfvdle4009"
    >
      <a
        class="hfpxzc"
        aria-label="Visa Application Centre"
        href="https://www.google.com/maps/place/Visa+Application+Centre/data=!4m7!3m6!1s0x14de11f725440157:0xb0d0266518447e12!8m2!3d35.168248!4d33.3462739!16s%2Fg%2F11s8k9gf0g!19sChIJVwFEJfcR3hQREn5EGGUm0LA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4009;focus:pane.wfvdle4009;blur:pane.wfvdle4009;auxclick:pane.wfvdle4009;keydown:pane.wfvdle4009;clickmod:pane.wfvdle4009"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJbXdFb0FBIixudWxsLDkwXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Visa Application Centre
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Metochiou 49</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4011;keydown:pane.wfvdle4011;mouseover:pane.wfvdle4011;mouseout:pane.wfvdle4011"
                aria-label="Visit Visa Application Centre's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJbXdFb0FBIiwiLEFPdlZhdzI2QU5wTnFQeDRhZ2NEZzhOZ1U2cEIsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0lxUUVvREEsIl0="
                href="https://www.vfsglobal.com/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4012;keydown:pane.wfvdle4012;mouseover:pane.wfvdle4012;mouseout:pane.wfvdle4012"
                aria-label="Get directions to Visa Application Centre"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJbXdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4013;mouseout:pane.wfvdle4013"
    >
      <a
        class="hfpxzc"
        aria-label="Υπηρεσία Διαχείρισης Επιδομάτων Πρόνοιας"
        href="https://www.google.com/maps/place/%CE%A5%CF%80%CE%B7%CF%81%CE%B5%CF%83%CE%AF%CE%B1+%CE%94%CE%B9%CE%B1%CF%87%CE%B5%CE%AF%CF%81%CE%B9%CF%83%CE%B7%CF%82+%CE%95%CF%80%CE%B9%CE%B4%CE%BF%CE%BC%CE%AC%CF%84%CF%89%CE%BD+%CE%A0%CF%81%CF%8C%CE%BD%CE%BF%CE%B9%CE%B1%CF%82/data=!4m7!3m6!1s0x14de1757ef2d8d47:0x1bebda1612dcedf2!8m2!3d35.1635857!4d33.3587124!16s%2Fg%2F11dfv47dz0!19sChIJR40t71cX3hQR8u3cEhba6xs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4013;focus:pane.wfvdle4013;blur:pane.wfvdle4013;auxclick:pane.wfvdle4013;keydown:pane.wfvdle4013;clickmod:pane.wfvdle4013"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJc2dFb0FBIixudWxsLDkxXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Υπηρεσία Διαχείρισης Επιδομάτων Πρόνοιας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.3 stars 25 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.3</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(25)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Themistokli Dervi 46</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 804000</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4015;keydown:pane.wfvdle4015;mouseover:pane.wfvdle4015;mouseout:pane.wfvdle4015"
                aria-label="Visit Υπηρεσία Διαχείρισης Επιδομάτων Πρόνοιας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJc2dFb0FBIiwiLEFPdlZhdzFSMG9RU0I4LVhfNEVlc3oydjZYSUMsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0l4QUVvRUEsIl0="
                href="http://www.wbas.dmsw.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4016;keydown:pane.wfvdle4016;mouseover:pane.wfvdle4016;mouseout:pane.wfvdle4016"
                aria-label="Get directions to Υπηρεσία Διαχείρισης Επιδομάτων Πρόνοιας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJc2dFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4017;mouseout:pane.wfvdle4017"
    >
      <a
        class="hfpxzc"
        aria-label="المبنى سبعين"
        href="https://www.google.com/maps/place/%D8%A7%D9%84%D9%85%D8%A8%D9%86%D9%89+%D8%B3%D8%A8%D8%B9%D9%8A%D9%86%E2%80%AD/data=!4m7!3m6!1s0x14de173cbb7b4887:0x4a0ae65c92bdd515!8m2!3d35.1608904!4d33.3680994!16s%2Fg%2F11vbbj2flg!19sChIJh0h7uzwX3hQRFdW9klzmCko?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4017;focus:pane.wfvdle4017;blur:pane.wfvdle4017;auxclick:pane.wfvdle4017;keydown:pane.wfvdle4017;clickmod:pane.wfvdle4017"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMmdFb0FBIixudWxsLDkyXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      <span dir="rtl">المبنى سبعين</span>
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Λεωφ. Αρχιεπισκόπου Μακαρίου Γ' 70</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4019;keydown:pane.wfvdle4019;mouseover:pane.wfvdle4019;mouseout:pane.wfvdle4019"
                aria-label="Get directions to المبنى سبعين"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMmdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4020;mouseout:pane.wfvdle4020"
    >
      <a
        class="hfpxzc"
        aria-label="Τμήμα Κτηματολογίου και Χωρομετρίας - Κεντρικά Γραφεία"
        href="https://www.google.com/maps/place/%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%9A%CF%84%CE%B7%CE%BC%CE%B1%CF%84%CE%BF%CE%BB%CE%BF%CE%B3%CE%AF%CE%BF%CF%85+%CE%BA%CE%B1%CE%B9+%CE%A7%CF%89%CF%81%CE%BF%CE%BC%CE%B5%CF%84%CF%81%CE%AF%CE%B1%CF%82+-+%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CE%AC+%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%B1/data=!4m7!3m6!1s0x14de17585e2e986b:0xfdfc51d790ec0a95!8m2!3d35.1632008!4d33.3559194!16s%2Fg%2F1hdz69wv0!19sChIJa5guXlgX3hQRlQrskNdR_P0?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4020;focus:pane.wfvdle4020;blur:pane.wfvdle4020;auxclick:pane.wfvdle4020;keydown:pane.wfvdle4020;clickmod:pane.wfvdle4020"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJN1FFb0FBIixudWxsLDkzXQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Τμήμα Κτηματολογίου και Χωρομετρίας - Κεντρικά Γραφεία
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.7 stars 11 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(11)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Iasonos 10</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:45 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 804900</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4022;keydown:pane.wfvdle4022;mouseover:pane.wfvdle4022;mouseout:pane.wfvdle4022"
                aria-label="Visit Τμήμα Κτηματολογίου και Χωρομετρίας - Κεντρικά Γραφεία's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJN1FFb0FBIiwiLEFPdlZhdzNNbjlWam9BOENMSFM0OGxuT0tqTkMsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0lfd0VvRUEsIl0="
                href="https://portal.dls.moi.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4023;keydown:pane.wfvdle4023;mouseover:pane.wfvdle4023;mouseout:pane.wfvdle4023"
                aria-label="Get directions to Τμήμα Κτηματολογίου και Χωρομετρίας - Κεντρικά Γραφεία"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJN1FFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4024;mouseout:pane.wfvdle4024"
    >
      <a
        class="hfpxzc"
        aria-label="Residence of British High Commissioner"
        href="https://www.google.com/maps/place/Residence+of+British+High+Commissioner/data=!4m7!3m6!1s0x14de174b61000001:0x6bc76ceb602649dc!8m2!3d35.1810013!4d33.3501929!16s%2Fg%2F11sskrlsx1!19sChIJAQAAYUsX3hQR3EkmYOtsx2s?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4024;focus:pane.wfvdle4024;blur:pane.wfvdle4024;auxclick:pane.wfvdle4024;keydown:pane.wfvdle4024;clickmod:pane.wfvdle4024"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJbEFJb0FBIixudWxsLDk0XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Residence of British High Commissioner
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Embassy</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59J2+C34, Müftü Dana Efendi Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4026;keydown:pane.wfvdle4026;mouseover:pane.wfvdle4026;mouseout:pane.wfvdle4026"
                aria-label="Get directions to Residence of British High Commissioner"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJbEFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4027;mouseout:pane.wfvdle4027"
    >
      <a
        class="hfpxzc"
        aria-label="Department for Town Planning and Housing"
        href="https://www.google.com/maps/place/Department+for+Town+Planning+and+Housing/data=!4m7!3m6!1s0x14de17521d2ad313:0xf2106d658cd87dbf!8m2!3d35.1741484!4d33.3540597!16s%2Fg%2F11c1nwzcv6!19sChIJE9MqHVIX3hQRv33YjGVtEPI?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4027;focus:pane.wfvdle4027;blur:pane.wfvdle4027;auxclick:pane.wfvdle4027;keydown:pane.wfvdle4027;clickmod:pane.wfvdle4027"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJcHdJb0FBIixudWxsLDk1XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Department for Town Planning and Housing
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="3.6 stars 5 Reviews"
                          ><span class="MW4etd" aria-hidden="true">3.6</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(5)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Τμήμα Πολεοδομίας και Οικήσεως, Kinyra 5-6</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 408100</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4029;keydown:pane.wfvdle4029;mouseover:pane.wfvdle4029;mouseout:pane.wfvdle4029"
                aria-label="Visit Department for Town Planning and Housing's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJcHdJb0FBIiwiLEFPdlZhdzNfdGctWGdiaEhCZUpEeDVBbjdrQm4sLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0l1d0lvRWcsIl0="
                href="https://www.moi.gov.cy/moi/tph/tph.nsf/home/home?openform"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4030;keydown:pane.wfvdle4030;mouseover:pane.wfvdle4030;mouseout:pane.wfvdle4030"
                aria-label="Get directions to Department for Town Planning and Housing"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJcHdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4031;mouseout:pane.wfvdle4031"
    >
      <a
        class="hfpxzc"
        aria-label="Τμήμα Εργασιακών Σχέσεων - Department of Labour Relations"
        href="https://www.google.com/maps/place/%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%95%CF%81%CE%B3%CE%B1%CF%83%CE%B9%CE%B1%CE%BA%CF%8E%CE%BD+%CE%A3%CF%87%CE%AD%CF%83%CE%B5%CF%89%CE%BD+-+Department+of+Labour+Relations/data=!4m7!3m6!1s0x14de1980ad468bbd:0xe644ff9d716c2b18!8m2!3d35.1639228!4d33.3529061!16s%2Fg%2F11jmxqvn2k!19sChIJvYtGrYAZ3hQRGCtscZ3_ROY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4031;focus:pane.wfvdle4031;blur:pane.wfvdle4031;auxclick:pane.wfvdle4031;keydown:pane.wfvdle4031;clickmod:pane.wfvdle4031"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMFFJb0FBIixudWxsLDk2XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Τμήμα Εργασιακών Σχέσεων - Department of Labour Relations
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Γεωρ. Γρίβα Διγενή 54-House, 2nd floor</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 803100</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4033;keydown:pane.wfvdle4033;mouseover:pane.wfvdle4033;mouseout:pane.wfvdle4033"
                aria-label="Visit Τμήμα Εργασιακών Σχέσεων - Department of Labour Relations's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMFFJb0FBIiwiLEFPdlZhdzFySi1Vb09JWFpGdVNlN1VyN3RLLUwsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0k0QUlvRGcsIl0="
                href="http://www.mlsi.gov.cy/dlr"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4034;keydown:pane.wfvdle4034;mouseover:pane.wfvdle4034;mouseout:pane.wfvdle4034"
                aria-label="Get directions to Τμήμα Εργασιακών Σχέσεων - Department of Labour Relations"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMFFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4035;mouseout:pane.wfvdle4035"
    >
      <a
        class="hfpxzc"
        aria-label="NICOSIA TOWN CENTER"
        href="https://www.google.com/maps/place/NICOSIA+TOWN+CENTER/data=!4m7!3m6!1s0x14de1773120097d5:0x8e08f8e84951d4a0!8m2!3d35.1694226!4d33.3618086!16s%2Fg%2F11g0mj22bg!19sChIJ1ZcAEnMX3hQRoNRRSej4CI4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4035;focus:pane.wfvdle4035;blur:pane.wfvdle4035;auxclick:pane.wfvdle4035;keydown:pane.wfvdle4035;clickmod:pane.wfvdle4035"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJOVFJb0FBIixudWxsLDk3XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      NICOSIA TOWN CENTER
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.7 stars 7 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(7)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City district office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5996+QP7</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4037;keydown:pane.wfvdle4037;mouseover:pane.wfvdle4037;mouseout:pane.wfvdle4037"
                aria-label="Get directions to NICOSIA TOWN CENTER"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJOVFJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4038;mouseout:pane.wfvdle4038"
    >
      <a
        class="hfpxzc"
        aria-label="Greek Embassy in Nicosia"
        href="https://www.google.com/maps/place/Greek+Embassy+in+Nicosia/data=!4m7!3m6!1s0x14de179bfd1c1975:0xfa94fbcebcef2964!8m2!3d35.1697595!4d33.3539847!16s%2Fg%2F11vbzk6nwz!19sChIJdRkc_ZsX3hQRZCnvvM77lPo?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4038;focus:pane.wfvdle4038;blur:pane.wfvdle4038;auxclick:pane.wfvdle4038;keydown:pane.wfvdle4038;clickmod:pane.wfvdle4038"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJamdNb0FBIixudWxsLDk4XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Greek Embassy in Nicosia
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5993+VHX</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4040;keydown:pane.wfvdle4040;mouseover:pane.wfvdle4040;mouseout:pane.wfvdle4040"
                aria-label="Get directions to Greek Embassy in Nicosia"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJamdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4041;mouseout:pane.wfvdle4041"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of Labour Employment Office"
        href="https://www.google.com/maps/place/Ministry+of+Labour+Employment+Office/data=!4m7!3m6!1s0x14de1751bdae9063:0x91c4a0798d5e85ac!8m2!3d35.1725384!4d33.3558827!16s%2Fg%2F11gfcy9ftv!19sChIJY5CuvVEX3hQRrIVejXmgxJE?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4041;focus:pane.wfvdle4041;blur:pane.wfvdle4041;auxclick:pane.wfvdle4041;keydown:pane.wfvdle4041;clickmod:pane.wfvdle4041"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJb2dNb0FBIixudWxsLDk5XQ=="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of Labour Employment Office
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.4 stars 12 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.4</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(12)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Unemployment office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Mouseiou 3</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 403000</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4043;keydown:pane.wfvdle4043;mouseover:pane.wfvdle4043;mouseout:pane.wfvdle4043"
                aria-label="Visit Ministry of Labour Employment Office's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJb2dNb0FBIiwiLEFPdlZhdzBxMkVvSXlKSGc3UFFxdXRxb0FDUk8sLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0l0QU1vRUEsIl0="
                href="http://www.mlsi.gov.cy/mlsi/dl/dl.nsf/index_gr/index_gr?OpenDocument"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4044;keydown:pane.wfvdle4044;mouseover:pane.wfvdle4044;mouseout:pane.wfvdle4044"
                aria-label="Get directions to Ministry of Labour Employment Office"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJb2dNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4045;mouseout:pane.wfvdle4045"
    >
      <a
        class="hfpxzc"
        aria-label="Selimiye Mahallesi Muhtarlığı"
        href="https://www.google.com/maps/place/Selimiye+Mahallesi+Muhtarl%C4%B1%C4%9F%C4%B1/data=!4m7!3m6!1s0x14de1744051991ad:0x7dbf1c94b8f30381!8m2!3d35.175814!4d33.364852!16s%2Fg%2F11bycggv66!19sChIJrZEZBUQX3hQRgQPzuJQcv30?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4045;focus:pane.wfvdle4045;blur:pane.wfvdle4045;auxclick:pane.wfvdle4045;keydown:pane.wfvdle4045;clickmod:pane.wfvdle4045"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJd0FNb0FBIixudWxsLDEwMF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Selimiye Mahallesi Muhtarlığı
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Uray Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4047;keydown:pane.wfvdle4047;mouseover:pane.wfvdle4047;mouseout:pane.wfvdle4047"
                aria-label="Get directions to Selimiye Mahallesi Muhtarlığı"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJd0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4048;mouseout:pane.wfvdle4048"
    >
      <a
        class="hfpxzc"
        aria-label="Κεντρικά Γραφεία Χωρομετρίας - Τμήμα Κτηματολογίου Χωρομετρίας"
        href="https://www.google.com/maps/place/%CE%9A%CE%B5%CE%BD%CF%84%CF%81%CE%B9%CE%BA%CE%AC+%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%B1+%CE%A7%CF%89%CF%81%CE%BF%CE%BC%CE%B5%CF%84%CF%81%CE%AF%CE%B1%CF%82+-+%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%9A%CF%84%CE%B7%CE%BC%CE%B1%CF%84%CE%BF%CE%BB%CE%BF%CE%B3%CE%AF%CE%BF%CF%85+%CE%A7%CF%89%CF%81%CE%BF%CE%BC%CE%B5%CF%84%CF%81%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de19d85e4b4099:0xa389d1623ec308f1!8m2!3d35.1610469!4d33.3634246!16s%2Fg%2F11gxxh8ccc!19sChIJmUBLXtgZ3hQR8QjDPmLRiaM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4048;focus:pane.wfvdle4048;blur:pane.wfvdle4048;auxclick:pane.wfvdle4048;keydown:pane.wfvdle4048;clickmod:pane.wfvdle4048"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMWdNb0FBIixudWxsLDEwMV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Κεντρικά Γραφεία Χωρομετρίας - Τμήμα Κτηματολογίου
                      Χωρομετρίας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Dimofontos 23a</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:45 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 402890</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4050;keydown:pane.wfvdle4050;mouseover:pane.wfvdle4050;mouseout:pane.wfvdle4050"
                aria-label="Visit Κεντρικά Γραφεία Χωρομετρίας - Τμήμα Κτηματολογίου Χωρομετρίας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMWdNb0FBIiwiLEFPdlZhdzNNbjlWam9BOENMSFM0OGxuT0tqTkMsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0k1Z01vRHcsIl0="
                href="https://portal.dls.moi.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4051;keydown:pane.wfvdle4051;mouseover:pane.wfvdle4051;mouseout:pane.wfvdle4051"
                aria-label="Get directions to Κεντρικά Γραφεία Χωρομετρίας - Τμήμα Κτηματολογίου Χωρομετρίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJMWdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4052;mouseout:pane.wfvdle4052"
    >
      <a
        class="hfpxzc"
        aria-label="Υπουργείο Εργασίας και Κοινωνικών Ασφαλίσεων - Ministry of Labour and Social Insurance"
        href="https://www.google.com/maps/place/%CE%A5%CF%80%CE%BF%CF%85%CF%81%CE%B3%CE%B5%CE%AF%CE%BF+%CE%95%CF%81%CE%B3%CE%B1%CF%83%CE%AF%CE%B1%CF%82+%CE%BA%CE%B1%CE%B9+%CE%9A%CE%BF%CE%B9%CE%BD%CF%89%CE%BD%CE%B9%CE%BA%CF%8E%CE%BD+%CE%91%CF%83%CF%86%CE%B1%CE%BB%CE%AF%CF%83%CE%B5%CF%89%CE%BD+-+Ministry+of+Labour+and+Social+Insurance/data=!4m7!3m6!1s0x14de19001efc8a01:0x18a7faa9f2b9f3c6!8m2!3d35.1640477!4d33.3622149!16s%2Fg%2F11vrwywvcl!19sChIJAYr8HgAZ3hQRxvO58qn6pxg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4052;focus:pane.wfvdle4052;blur:pane.wfvdle4052;auxclick:pane.wfvdle4052;keydown:pane.wfvdle4052;clickmod:pane.wfvdle4052"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJLXdNb0FBIixudWxsLDEwMl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Υπουργείο Εργασίας και Κοινωνικών Ασφαλίσεων - Ministry of
                      Labour and Social Insurance
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5976+JV8, Spyrou Kyprianou Avenue</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 401600</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4054;keydown:pane.wfvdle4054;mouseover:pane.wfvdle4054;mouseout:pane.wfvdle4054"
                aria-label="Visit Υπουργείο Εργασίας και Κοινωνικών Ασφαλίσεων - Ministry of Labour and Social Insurance's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJLXdNb0FBIiwiLEFPdlZhdzBicDlJRlQ2TmFpUDRjc0cwZndIRVMsLDBhaFVLRXdpNm5lM3V4WUNHQXhXS2NQRURIVnNUQnJZUTYxZ0lqUVFvRVEsIl0="
                href="https://www.mlsi.gov.cy/mlsi/mlsi.nsf/home-el/home-el?OpenForm"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4055;keydown:pane.wfvdle4055;mouseover:pane.wfvdle4055;mouseout:pane.wfvdle4055"
                aria-label="Get directions to Υπουργείο Εργασίας και Κοινωνικών Ασφαλίσεων - Ministry of Labour and Social Insurance"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJLXdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4056;mouseout:pane.wfvdle4056"
    >
      <a
        class="hfpxzc"
        aria-label="Embassy of Hungary"
        href="https://www.google.com/maps/place/Embassy+of+Hungary/data=!4m7!3m6!1s0x14de1748be85bec9:0x71a805563ad616f1!8m2!3d35.1664194!4d33.3692163!16s%2Fg%2F11s4_b7ybp!19sChIJyb6FvkgX3hQR8RbWOlYFqHE?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4056;focus:pane.wfvdle4056;blur:pane.wfvdle4056;auxclick:pane.wfvdle4056;keydown:pane.wfvdle4056;clickmod:pane.wfvdle4056"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJb3dRb0FBIixudWxsLDEwM10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Embassy of Hungary
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Digeni Akrita 58-48</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4058;keydown:pane.wfvdle4058;mouseover:pane.wfvdle4058;mouseout:pane.wfvdle4058"
                aria-label="Get directions to Embassy of Hungary"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJb3dRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4059;mouseout:pane.wfvdle4059"
    >
      <a
        class="hfpxzc"
        aria-label="Devlet Üretme Çiftlikleri Dairesi"
        href="https://www.google.com/maps/place/Devlet+%C3%9Cretme+%C3%87iftlikleri+Dairesi/data=!4m7!3m6!1s0x14de17460172b49b:0x46a160abac2397f0!8m2!3d35.1780221!4d33.3600515!16s%2Fg%2F1w0mdzlb!19sChIJm7RyAUYX3hQR8JcjrKtgoUY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4059;focus:pane.wfvdle4059;blur:pane.wfvdle4059;auxclick:pane.wfvdle4059;keydown:pane.wfvdle4059;clickmod:pane.wfvdle4059"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJdHdRb0FBIixudWxsLDEwNF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Devlet Üretme Çiftlikleri Dairesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Livestock breeder</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59H6+623, Sarayönü Sk</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4061;keydown:pane.wfvdle4061;mouseover:pane.wfvdle4061;mouseout:pane.wfvdle4061"
                aria-label="Get directions to Devlet Üretme Çiftlikleri Dairesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aTZuZTN1eFlDR0F4V0tjUEVESFZzVEJyWVE4QmNJdHdRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4062;mouseout:pane.wfvdle4062"
    >
      <a
        class="hfpxzc"
        aria-label="Swedish embassy"
        href="https://www.google.com/maps/place/Swedish+embassy/data=!4m7!3m6!1s0x14de17f989900fdf:0xa5d618973ee710b1!8m2!3d35.1682517!4d33.3601434!16s%2Fg%2F11q8tmfxq2!19sChIJ3w-QifkX3hQRsRDnPpcY1qU?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4062;focus:pane.wfvdle4062;blur:pane.wfvdle4062;auxclick:pane.wfvdle4062;keydown:pane.wfvdle4062;clickmod:pane.wfvdle4062"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJQlNnQSIsbnVsbCwxMDZd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">Swedish embassy</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >9, Arch. Makarios III Avenue Severis Building, 2nd
                          floor 1065</span
                        ></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4064;keydown:pane.wfvdle4064;mouseover:pane.wfvdle4064;mouseout:pane.wfvdle4064"
                aria-label="Get directions to Swedish embassy"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJQlNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4065;mouseout:pane.wfvdle4065"
    >
      <a
        class="hfpxzc"
        aria-label="LNG Danışmanlık"
        href="https://www.google.com/maps/place/LNG+Dan%C4%B1%C5%9Fmanl%C4%B1k/data=!4m7!3m6!1s0x14de17e9f52c1b3d:0xad4718d5e2a243fc!8m2!3d35.1799784!4d33.3597654!16s%2Fg%2F11sgc677t2!19sChIJPRss9ekX3hQR_EOi4tUYR60?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4065;focus:pane.wfvdle4065;blur:pane.wfvdle4065;auxclick:pane.wfvdle4065;keydown:pane.wfvdle4065;clickmod:pane.wfvdle4065"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJR0NnQSIsbnVsbCwxMDdd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">LNG Danışmanlık</div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Visa and passport office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Mahmut Paşa Sk Mahmut Paşa Kapalı Otopark, Altı No
                          95</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 6 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 533 845 45 55</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4067;keydown:pane.wfvdle4067;mouseover:pane.wfvdle4067;mouseout:pane.wfvdle4067"
                aria-label="Get directions to LNG Danışmanlık"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJR0NnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4068;mouseout:pane.wfvdle4068"
    >
      <a
        class="hfpxzc"
        aria-label="Γραφείο Επιτρόπου Προστασίας Δεδομένων Προσωπικού Χαρακτήρα"
        href="https://www.google.com/maps/place/%CE%93%CF%81%CE%B1%CF%86%CE%B5%CE%AF%CE%BF+%CE%95%CF%80%CE%B9%CF%84%CF%81%CF%8C%CF%80%CE%BF%CF%85+%CE%A0%CF%81%CE%BF%CF%83%CF%84%CE%B1%CF%83%CE%AF%CE%B1%CF%82+%CE%94%CE%B5%CE%B4%CE%BF%CE%BC%CE%AD%CE%BD%CF%89%CE%BD+%CE%A0%CF%81%CE%BF%CF%83%CF%89%CF%80%CE%B9%CE%BA%CE%BF%CF%8D+%CE%A7%CE%B1%CF%81%CE%B1%CE%BA%CF%84%CE%AE%CF%81%CE%B1/data=!4m7!3m6!1s0x14de17001480ee03:0x406e0db706cc7041!8m2!3d35.1652107!4d33.3653521!16s%2Fg%2F11y2x_h4dq!19sChIJA-6AFAAX3hQRQXDMBrcNbkA?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4068;focus:pane.wfvdle4068;blur:pane.wfvdle4068;auxclick:pane.wfvdle4068;keydown:pane.wfvdle4068;clickmod:pane.wfvdle4068"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJT3lnQSIsbnVsbCwxMDhd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Γραφείο Επιτρόπου Προστασίας Δεδομένων Προσωπικού
                      Χαρακτήρα
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Kypranoros 15</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 818456</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4070;keydown:pane.wfvdle4070;mouseover:pane.wfvdle4070;mouseout:pane.wfvdle4070"
                aria-label="Visit Γραφείο Επιτρόπου Προστασίας Δεδομένων Προσωπικού Χαρακτήρα's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJT3lnQSIsIixBT3ZWYXczSGhlQ2IyQU5KMnlDYXB1N2VHUWhXLCwwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E2MWdJU3lnUCwiXQ=="
                href="http://www.dataprotection.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4071;keydown:pane.wfvdle4071;mouseover:pane.wfvdle4071;mouseout:pane.wfvdle4071"
                aria-label="Get directions to Γραφείο Επιτρόπου Προστασίας Δεδομένων Προσωπικού Χαρακτήρα"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJT3lnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4072;mouseout:pane.wfvdle4072"
    >
      <a
        class="hfpxzc"
        aria-label="Kamu Hizmeti Komüsyonu"
        href="https://www.google.com/maps/place/Kamu+Hizmeti+Kom%C3%BCsyonu/data=!4m7!3m6!1s0x14de17479d456c87:0x9bbc752c2d0ba46a!8m2!3d35.181241!4d33.362591!16s%2Fg%2F11b7q81sq4!19sChIJh2xFnUcX3hQRaqQLLSx1vJs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4072;focus:pane.wfvdle4072;blur:pane.wfvdle4072;auxclick:pane.wfvdle4072;keydown:pane.wfvdle4072;clickmod:pane.wfvdle4072"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJVkNnQSIsbnVsbCwxMDld"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kamu Hizmeti Komüsyonu
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Local government office</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4074;keydown:pane.wfvdle4074;mouseover:pane.wfvdle4074;mouseout:pane.wfvdle4074"
                aria-label="Get directions to Kamu Hizmeti Komüsyonu"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJVkNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4075;mouseout:pane.wfvdle4075"
    >
      <a
        class="hfpxzc"
        aria-label="National Betting Authority"
        href="https://www.google.com/maps/place/National+Betting+Authority/data=!4m7!3m6!1s0x14de17f694958e4b:0x7b3db234ca1c9ab5!8m2!3d35.1645212!4d33.3653787!16s%2Fg%2F11fn261d8k!19sChIJS46VlPYX3hQRtZocyjSyPXs?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4075;focus:pane.wfvdle4075;blur:pane.wfvdle4075;auxclick:pane.wfvdle4075;keydown:pane.wfvdle4075;clickmod:pane.wfvdle4075"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJWkNnQSIsbnVsbCwxMTBd"
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      National Betting Authority
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Digeni Akrita 83</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 881800</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4077;keydown:pane.wfvdle4077;mouseover:pane.wfvdle4077;mouseout:pane.wfvdle4077"
                aria-label="Visit National Betting Authority's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJWkNnQSIsIixBT3ZWYXcyVWowaU9nV2pYQW5KV1pWczhwcThHLCwwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E2MWdJZENnUCwiXQ=="
                href="http://www.nba.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4078;keydown:pane.wfvdle4078;mouseover:pane.wfvdle4078;mouseout:pane.wfvdle4078"
                aria-label="Get directions to National Betting Authority"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJWkNnQSJd"
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4079;mouseout:pane.wfvdle4079"
    >
      <a
        class="hfpxzc"
        aria-label="Υπηρεσια Φοιτητικής Μέριμνας"
        href="https://www.google.com/maps/place/%CE%A5%CF%80%CE%B7%CF%81%CE%B5%CF%83%CE%B9%CE%B1+%CE%A6%CE%BF%CE%B9%CF%84%CE%B7%CF%84%CE%B9%CE%BA%CE%AE%CF%82+%CE%9C%CE%AD%CF%81%CE%B9%CE%BC%CE%BD%CE%B1%CF%82/data=!4m7!3m6!1s0x14de1757daf3d287:0x256fae5c90eb59aa!8m2!3d35.1643872!4d33.3578186!16s%2Fg%2F11c55s85z1!19sChIJh9Lz2lcX3hQRqlnrkFyubyU?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4079;focus:pane.wfvdle4079;blur:pane.wfvdle4079;auxclick:pane.wfvdle4079;keydown:pane.wfvdle4079;clickmod:pane.wfvdle4079"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJaGdFb0FBIixudWxsLDExMV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Υπηρεσια Φοιτητικής Μέριμνας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.4 stars 44 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.4</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(44)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Tefkrou 6</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 804002</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4081;keydown:pane.wfvdle4081;mouseover:pane.wfvdle4081;mouseout:pane.wfvdle4081"
                aria-label="Get directions to Υπηρεσια Φοιτητικής Μέριμνας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJaGdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4082;mouseout:pane.wfvdle4082"
    >
      <a
        class="hfpxzc"
        aria-label="Kyrenia Municipality"
        href="https://www.google.com/maps/place/Kyrenia+Municipality/data=!4m7!3m6!1s0x14de174e7155d72d:0x990b00b00b99295d!8m2!3d35.1761931!4d33.3548994!16s%2Fg%2F11c5fzxnlf!19sChIJLddVcU4X3hQRXSmZC7AAC5k?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4082;focus:pane.wfvdle4082;blur:pane.wfvdle4082;auxclick:pane.wfvdle4082;keydown:pane.wfvdle4082;clickmod:pane.wfvdle4082"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJclFFb0FBIixudWxsLDExMl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Kyrenia Municipality
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="4.2 stars 5 Reviews"
                          ><span class="MW4etd" aria-hidden="true">4.2</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(5)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>City Hall</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Nicosia, Markou Drakou</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 818040</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4084;keydown:pane.wfvdle4084;mouseover:pane.wfvdle4084;mouseout:pane.wfvdle4084"
                aria-label="Visit Kyrenia Municipality's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJclFFb0FBIiwiLEFPdlZhdzNXZUswT2p6YV9QdlhVSnlfTDNsUG8sLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0l3UUVvRWcsIl0="
                href="http://www.kyreniamunicipality.com/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4085;keydown:pane.wfvdle4085;mouseover:pane.wfvdle4085;mouseout:pane.wfvdle4085"
                aria-label="Get directions to Kyrenia Municipality"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJclFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4086;mouseout:pane.wfvdle4086"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of the Interior"
        href="https://www.google.com/maps/place/Ministry+of+the+Interior/data=!4m7!3m6!1s0x14de1755dd878c85:0xa6a5ae3f712b04dd!8m2!3d35.1663648!4d33.3540488!16s%2Fg%2F1tf2hsbw!19sChIJhYyH3VUX3hQR3QQrcT-upaY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4086;focus:pane.wfvdle4086;blur:pane.wfvdle4086;auxclick:pane.wfvdle4086;keydown:pane.wfvdle4086;clickmod:pane.wfvdle4086"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJelFFb0FBIixudWxsLDExM10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of the Interior
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.7 stars 20 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(20)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span
                          >Διεύθυνση Υπουργείου Εσωτερικών Υπουργείο
                          Εσωτερικών</span
                        ></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 867600</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4088;keydown:pane.wfvdle4088;mouseover:pane.wfvdle4088;mouseout:pane.wfvdle4088"
                aria-label="Visit Ministry of the Interior's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJelFFb0FBIiwiLEFPdlZhdzBIWFVZaEVOWXBvQ3BsU2VkTzFvMVgsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0kzZ0VvRHcsIl0="
                href="http://www.moi.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4089;keydown:pane.wfvdle4089;mouseover:pane.wfvdle4089;mouseout:pane.wfvdle4089"
                aria-label="Get directions to Ministry of the Interior"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJelFFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4090;mouseout:pane.wfvdle4090"
    >
      <a
        class="hfpxzc"
        aria-label="Τμήμα Πολιτικής Αεροπορίας"
        href="https://www.google.com/maps/place/%CE%A4%CE%BC%CE%AE%CE%BC%CE%B1+%CE%A0%CE%BF%CE%BB%CE%B9%CF%84%CE%B9%CE%BA%CE%AE%CF%82+%CE%91%CE%B5%CF%81%CE%BF%CF%80%CE%BF%CF%81%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de177eef66483f:0xd31e31a209482ab5!8m2!3d35.1664653!4d33.367307!16s%2Fg%2F11h7yf07cm!19sChIJP0hm734X3hQRtSpICaIxHtM?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4090;focus:pane.wfvdle4090;blur:pane.wfvdle4090;auxclick:pane.wfvdle4090;keydown:pane.wfvdle4090;clickmod:pane.wfvdle4090"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdFb0FBIixudWxsLDExNF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Τμήμα Πολιτικής Αεροπορίας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5988+HWM, Dimitri Vikela</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 404102</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4092;keydown:pane.wfvdle4092;mouseover:pane.wfvdle4092;mouseout:pane.wfvdle4092"
                aria-label="Visit Τμήμα Πολιτικής Αεροπορίας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdFb0FBIiwiLEFPdlZhdzFrLVlKR1dycW5DWXphVl9fVXpRR0ksLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0loUUlvRVEsIl0="
                href="http://www.mcw.gov.cy/mcw/dca/dca.nsf/DMLindex_gr/DMLindex_gr?OpenDocument"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4093;keydown:pane.wfvdle4093;mouseover:pane.wfvdle4093;mouseout:pane.wfvdle4093"
                aria-label="Get directions to Τμήμα Πολιτικής Αεροπορίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdFb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4094;mouseout:pane.wfvdle4094"
    >
      <a
        class="hfpxzc"
        aria-label="Ελεγκτική Υπηρεσία της Δημοκρατίας"
        href="https://www.google.com/maps/place/%CE%95%CE%BB%CE%B5%CE%B3%CE%BA%CF%84%CE%B9%CE%BA%CE%AE+%CE%A5%CF%80%CE%B7%CF%81%CE%B5%CF%83%CE%AF%CE%B1+%CF%84%CE%B7%CF%82+%CE%94%CE%B7%CE%BC%CE%BF%CE%BA%CF%81%CE%B1%CF%84%CE%AF%CE%B1%CF%82/data=!4m7!3m6!1s0x14de19fd8b43cba3:0x6c52058561867ceb!8m2!3d35.1640217!4d33.3555517!16s%2Fg%2F11f_j9538z!19sChIJo8tDi_0Z3hQR63yGYYUFUmw?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4094;focus:pane.wfvdle4094;blur:pane.wfvdle4094;auxclick:pane.wfvdle4094;keydown:pane.wfvdle4094;clickmod:pane.wfvdle4094"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJamdJb0FBIixudWxsLDExNV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ελεγκτική Υπηρεσία της Δημοκρατίας
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 3 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(3)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>State government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Deligiorgi 6</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7:30 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 401463</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4096;keydown:pane.wfvdle4096;mouseover:pane.wfvdle4096;mouseout:pane.wfvdle4096"
                aria-label="Visit Ελεγκτική Υπηρεσία της Δημοκρατίας's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJamdJb0FBIiwiLEFPdlZhdzFWdW40dmFIWXpoSVhwdzFxZzZaXzAsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0lvQUlvRUEsIl0="
                href="http://www.audit.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4097;keydown:pane.wfvdle4097;mouseover:pane.wfvdle4097;mouseout:pane.wfvdle4097"
                aria-label="Get directions to Ελεγκτική Υπηρεσία της Δημοκρατίας"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJamdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4098;mouseout:pane.wfvdle4098"
    >
      <a
        class="hfpxzc"
        aria-label="Μονάδα Ευρωπαικών Ταμείων - European Funds Unit"
        href="https://www.google.com/maps/place/%CE%9C%CE%BF%CE%BD%CE%AC%CE%B4%CE%B1+%CE%95%CF%85%CF%81%CF%89%CF%80%CE%B1%CE%B9%CE%BA%CF%8E%CE%BD+%CE%A4%CE%B1%CE%BC%CE%B5%CE%AF%CF%89%CE%BD+-+European+Funds+Unit/data=!4m7!3m6!1s0x14de1706f2a15521:0x5f110eacba519b9b!8m2!3d35.1661574!4d33.3605707!16s%2Fg%2F11gxmhfw8n!19sChIJIVWh8gYX3hQRm5tRuqwOEV8?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4098;focus:pane.wfvdle4098;blur:pane.wfvdle4098;auxclick:pane.wfvdle4098;keydown:pane.wfvdle4098;clickmod:pane.wfvdle4098"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJc2dJb0FBIixudWxsLDExNl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Μονάδα Ευρωπαικών Ταμείων - European Funds Unit
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 2 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(2)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Mnasiadou 10 1065</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 7 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 409999</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4100;keydown:pane.wfvdle4100;mouseover:pane.wfvdle4100;mouseout:pane.wfvdle4100"
                aria-label="Visit Μονάδα Ευρωπαικών Ταμείων - European Funds Unit's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJc2dJb0FBIiwiLEFPdlZhdzBiSkN0M0VCSWtDbWR4SGUza1lkQlAsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0l4QUlvRUEsIl0="
                href="http://www.moi.gov.cy/efu"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4101;keydown:pane.wfvdle4101;mouseover:pane.wfvdle4101;mouseout:pane.wfvdle4101"
                aria-label="Get directions to Μονάδα Ευρωπαικών Ταμείων - European Funds Unit"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJc2dJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4102;mouseout:pane.wfvdle4102"
    >
      <a
        class="hfpxzc"
        aria-label="Department of Civil Aviation Cyprus (DCAC)"
        href="https://www.google.com/maps/place/Department+of+Civil+Aviation+Cyprus+%28DCAC%29/data=!4m7!3m6!1s0x14de175c17a3a83d:0xa82a7dbfc12f85dc!8m2!3d35.1666487!4d33.3667069!16s%2Fg%2F11g8b55f8b!19sChIJPaijF1wX3hQR3IUvwb99Kqg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4102;focus:pane.wfvdle4102;blur:pane.wfvdle4102;auxclick:pane.wfvdle4102;keydown:pane.wfvdle4102;clickmod:pane.wfvdle4102"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJMXdJb0FBIixudWxsLDExN10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Department of Civil Aviation Cyprus (DCAC)
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5988+MM4, Pindarou</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="font-weight: 400; color: rgba(176, 96, 0, 1)"
                            >Closes soon</span
                          ><span style="font-weight: 400">
                            ⋅ 4 PM ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 404102</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4104;keydown:pane.wfvdle4104;mouseover:pane.wfvdle4104;mouseout:pane.wfvdle4104"
                aria-label="Visit Department of Civil Aviation Cyprus (DCAC)'s website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJMXdJb0FBIiwiLEFPdlZhdzF4MUE3ZjR3OTVCS3QwVzJCRDk2NHgsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0k2UUlvRVEsIl0="
                href="http://www.mcw.gov.cy/dca"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4105;keydown:pane.wfvdle4105;mouseover:pane.wfvdle4105;mouseout:pane.wfvdle4105"
                aria-label="Get directions to Department of Civil Aviation Cyprus (DCAC)"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJMXdJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4106;mouseout:pane.wfvdle4106"
    >
      <a
        class="hfpxzc"
        aria-label="Οικογενειακό Δικαστήριο Λευκωσίας / Family Court Nicosia"
        href="https://www.google.com/maps/place/%CE%9F%CE%B9%CE%BA%CE%BF%CE%B3%CE%B5%CE%BD%CE%B5%CE%B9%CE%B1%CE%BA%CF%8C+%CE%94%CE%B9%CE%BA%CE%B1%CF%83%CF%84%CE%AE%CF%81%CE%B9%CE%BF+%CE%9B%CE%B5%CF%85%CE%BA%CF%89%CF%83%CE%AF%CE%B1%CF%82+%2F+Family+Court+Nicosia/data=!4m7!3m6!1s0x14de17ac40437837:0xf85d5ee3763687a0!8m2!3d35.169034!4d33.357964!16s%2Fg%2F11pcdnthlx!19sChIJN3hDQKwX3hQRoIc2duNeXfg?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4106;focus:pane.wfvdle4106;blur:pane.wfvdle4106;auxclick:pane.wfvdle4106;keydown:pane.wfvdle4106;clickmod:pane.wfvdle4106"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJX0FJb0FBIixudWxsLDExOF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Οικογενειακό Δικαστήριο Λευκωσίας / Family Court Nicosia
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>District government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Diagorou 27</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+357 22 369717</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4108;keydown:pane.wfvdle4108;mouseover:pane.wfvdle4108;mouseout:pane.wfvdle4108"
                aria-label="Visit Οικογενειακό Δικαστήριο Λευκωσίας / Family Court Nicosia's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJX0FJb0FBIiwiLEFPdlZhdzJhZmJOdlluTUQtbHNoNlVjVzJ5YWIsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0lqQU1vRHcsIl0="
                href="http://www.supremecourt.gov.cy/judicial/sc.nsf/DMLFcourt_gr/DMLFcourt_gr?opendocument"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4109;keydown:pane.wfvdle4109;mouseover:pane.wfvdle4109;mouseout:pane.wfvdle4109"
                aria-label="Get directions to Οικογενειακό Δικαστήριο Λευκωσίας / Family Court Nicosia"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJX0FJb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4110;mouseout:pane.wfvdle4110"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of Health."
        href="https://www.google.com/maps/place/Ministry+of+Health./data=!4m7!3m6!1s0x14de1754dcf5dc91:0xe678f1a4b53cc132!8m2!3d35.1693158!4d33.349453!16s%2Fg%2F1tf9km3r!19sChIJkdz13FQX3hQRMsE8taTxeOY?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4110;focus:pane.wfvdle4110;blur:pane.wfvdle4110;auxclick:pane.wfvdle4110;keydown:pane.wfvdle4110;clickmod:pane.wfvdle4110"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFNb0FBIixudWxsLDExOV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of Health.
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="1.7 stars 139 Reviews"
                          ><span class="MW4etd" aria-hidden="true">1.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(139)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Prodromou 1</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 605300</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4112;keydown:pane.wfvdle4112;mouseover:pane.wfvdle4112;mouseout:pane.wfvdle4112"
                aria-label="Visit Ministry of Health.'s website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFNb0FBIiwiLEFPdlZhdzNJTnI4Wmx5N2VGYkZ1Z01LOVdpb1MsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0lxZ01vRUEsIl0="
                href="http://www.moh.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4113;keydown:pane.wfvdle4113;mouseover:pane.wfvdle4113;mouseout:pane.wfvdle4113"
                aria-label="Get directions to Ministry of Health."
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4114;mouseout:pane.wfvdle4114"
    >
      <a
        class="hfpxzc"
        aria-label="Küçükkaymaklı Posta Şubesi"
        href="https://www.google.com/maps/place/K%C3%BC%C3%A7%C3%BCkkaymakl%C4%B1+Posta+%C5%9Eubesi/data=!4m7!3m6!1s0x14de1739442e2857:0x19b05148f54b499b!8m2!3d35.1853004!4d33.3645397!16s%2Fg%2F1tcynwxy!19sChIJVyguRDkX3hQRm0lL9UhRsBk?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4114;focus:pane.wfvdle4114;blur:pane.wfvdle4114;auxclick:pane.wfvdle4114;keydown:pane.wfvdle4114;clickmod:pane.wfvdle4114"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJd0FNb0FBIixudWxsLDEyMF0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Küçükkaymaklı Posta Şubesi
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.8 stars 6 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.8</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(6)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Post office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>59P7+4RF, Kızılay Sk</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span><span class="UsdlK">+90 392 227 73 40</span></span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4116;keydown:pane.wfvdle4116;mouseover:pane.wfvdle4116;mouseout:pane.wfvdle4116"
                aria-label="Get directions to Küçükkaymaklı Posta Şubesi"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJd0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK Q2HXcd THOPZb"
      jsaction="mouseover:pane.wfvdle4117;mouseout:pane.wfvdle4117"
    >
      <a
        class="hfpxzc"
        aria-label="UN Bufferzone Checkpoint (not passable)"
        href="https://www.google.com/maps/place/UN+Bufferzone+Checkpoint+%28not+passable%29/data=!4m7!3m6!1s0x14de17ffb2d48319:0x92766c7f0f2a029b!8m2!3d35.1756627!4d33.3677136!16s%2Fg%2F11sb4z00_y!19sChIJGYPUsv8X3hQRmwIqD39sdpI?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4117;focus:pane.wfvdle4117;blur:pane.wfvdle4117;auxclick:pane.wfvdle4117;keydown:pane.wfvdle4117;clickmod:pane.wfvdle4117"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJM0FNb0FBIixudWxsLDEyMV0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      UN Bufferzone Checkpoint (not passable)
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium">No reviews</span>
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Ermou 257</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4119;keydown:pane.wfvdle4119;mouseover:pane.wfvdle4119;mouseout:pane.wfvdle4119"
                aria-label="Get directions to UN Bufferzone Checkpoint (not passable)"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJM0FNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4120;mouseout:pane.wfvdle4120"
    >
      <a
        class="hfpxzc"
        aria-label="Erenköy Tourist Information Centre"
        href="https://www.google.com/maps/place/Erenk%C3%B6y+Tourist+Information+Centre/data=!4m7!3m6!1s0x14df6df149ce4959:0x457c72333237520d!8m2!3d35.5348477!4d34.1888416!16s%2Fg%2F11s42qrdr7!19sChIJWUnOSfFt3xQRDVI3MjNyfEU?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4120;focus:pane.wfvdle4120;blur:pane.wfvdle4120;auxclick:pane.wfvdle4120;keydown:pane.wfvdle4120;clickmod:pane.wfvdle4120"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdNb0FBIixudWxsLDEyMl0="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Erenköy Tourist Information Centre
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="5.0 stars 1 Reviews"
                          ><span class="MW4etd" aria-hidden="true">5.0</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(1)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Government office</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>Ecevit caddesi no 10</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(24, 128, 56, 1);
                            "
                            >Open</span
                          ><span style="font-weight: 400">
                            ⋅ Closes 7 PM</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+90 392 374 49 84</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4122;keydown:pane.wfvdle4122;mouseover:pane.wfvdle4122;mouseout:pane.wfvdle4122"
                aria-label="Visit Erenköy Tourist Information Centre's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdNb0FBIiwiLEFPdlZhdzNJY1ZndGRueHQzOE1NNWhianl6V08sLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0lnZ1FvRFEsIl0="
                href="http://www.visitncy.com/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4123;keydown:pane.wfvdle4123;mouseover:pane.wfvdle4123;mouseout:pane.wfvdle4123"
                aria-label="Get directions to Erenköy Tourist Information Centre"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJOHdNb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div class="TFQHme"></div>
  <div>
    <div
      class="Nv2PK tH5CWc THOPZb"
      jsaction="mouseover:pane.wfvdle4124;mouseout:pane.wfvdle4124"
    >
      <a
        class="hfpxzc"
        aria-label="Ministry of Finance"
        href="https://www.google.com/maps/place/Ministry+of+Finance/data=!4m7!3m6!1s0x14de1756805066c5:0x5eaa3310eddc2ca5!8m2!3d35.1674718!4d33.3544012!16s%2Fg%2F1tfj5d8g!19sChIJxWZQgFYX3hQRpSzc7RAzql4?authuser=0&amp;hl=en&amp;rclk=1"
        jsaction="pane.wfvdle4124;focus:pane.wfvdle4124;blur:pane.wfvdle4124;auxclick:pane.wfvdle4124;keydown:pane.wfvdle4124;clickmod:pane.wfvdle4124"
        jslog="12690;track:click,contextmenu;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFRb0FBIixudWxsLDEyM10="
      ></a>
      <div class="rWbY0d"></div>
      <div class="bfdHYd Ppzolf OFBs3e">
        <div class="rgFiGf OyjIsf"></div>
        <div class="hHbUWd"></div>
        <div class="rSy5If"></div>
        <div class="lI9IFe">
          <div class="y7PRA">
            <div class="Lui3Od T7Wufd">
              <div class="Z8fK3b">
                <div class="OyjIsf"></div>
                <div class="UaQhfb fontBodyMedium">
                  <div class="NrDZNb">
                    <div class="dIDW9d"></div>
                    <span class="HTCGSb"></span>
                    <div class="qBF1Pd fontHeadlineSmall">
                      Ministry of Finance
                    </div>
                    <span class="muMOJe"></span>
                  </div>
                  <div class="section-subtitle-extension"></div>
                  <div class="W4Efsd">
                    <div class="AJB7ye">
                      <span class="wZrhX"></span>
                      <span class="e4rVHe fontBodyMedium"
                        ><span
                          role="img"
                          class="ZkP5Je"
                          aria-label="2.7 stars 19 Reviews"
                          ><span class="MW4etd" aria-hidden="true">2.7</span>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c"></div>
                          <div class="QBUL8c vIBWLc"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <div class="QBUL8c B53l4e"></div>
                          <span class="UY7F9" aria-hidden="true"
                            >(19)</span
                          ></span
                        ></span
                      >
                    </div>
                  </div>
                  <div class="W4Efsd">
                    <div class="W4Efsd">
                      <span><span>Tax department</span></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span>5983+XQJ, Grigori Afxentiou</span></span
                      >
                    </div>
                    <div class="W4Efsd">
                      <span
                        ><span
                          ><span
                            style="
                              font-weight: 400;
                              color: rgba(217, 48, 37, 1);
                            "
                            >Closed</span
                          ><span style="font-weight: 400">
                            ⋅ Opens 8 AM Fri</span
                          ></span
                        ></span
                      ><span>
                        <span aria-hidden="true">·</span>
                        <span class="UsdlK">+357 22 602722</span></span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="Rwjeuc">
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <a
                class="lcr4fd S9kvJb"
                jsaction="pane.wfvdle4126;keydown:pane.wfvdle4126;mouseover:pane.wfvdle4126;mouseout:pane.wfvdle4126"
                aria-label="Visit Ministry of Finance's website"
                data-value="Website"
                jslog="84919;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFRb0FBIiwiLEFPdlZhdzA2S3NOdWN5MkwzVXl6UEIwMzR6VUcsLDBhaFVLRXdpcjR2RHZ4WUNHQXhXOVZ2RURIWldCQmtnUTYxZ0lyQVFvRWcsIl0="
                href="http://mof.gov.cy/"
                ><span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Website</div></a
              >
            </div>
            <div class="etWJQ jym1ob kdfrQc bWQG4d">
              <button
                class="g88MCb S9kvJb"
                jsaction="pane.wfvdle4127;keydown:pane.wfvdle4127;mouseover:pane.wfvdle4127;mouseout:pane.wfvdle4127"
                aria-label="Get directions to Ministry of Finance"
                data-value="Directions"
                jslog="80860;track:click;mutable:true;metadata:WyIwYWhVS0V3aXI0dkR2eFlDR0F4VzlWdkVESFpXQkJrZ1E4QmNJbUFRb0FBIl0="
              >
                <span class="DVeyrd"
                  ><div class="OyjIsf zemfqc"></div>
                  <span
                    class="Cw1rxd google-symbols G47vBd PHazN"
                    aria-hidden="true"
                    style="font-size: 18px"
                    ></span
                  ></span
                >
                <div class="R8c4Qb fontBodySmall">Directions</div>
              </button>
            </div>
          </div>
          <div class="SpFAAb"></div>
        </div>
        <div class="qty3Ue"></div>
        <div class="gwQ6lc" jsaction="click:mLt3mc"></div>
      </div>
    </div>
  </div>
  <div></div>
  <div class="m6QErb tLjsW eKbjU" style="height: 64px; padding: 16px 67px">
    <div class="PbZDve">
      <p class="fontBodyMedium">
        <span
          ><span class="HlvSq">You've reached the end of the list.</span></span
        >
      </p>
    </div>
  </div>
</div>
'''
def extract_restaurant_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    official = []
    for div in soup.find_all('div', class_='Nv2PK tH5CWc THOPZb'):
        name = div.parent.find('a', class_='hfpxzc')['aria-label']
        image_tag = div.find_next('img')
        image_url = image_tag['src'] if image_tag else None
        href = div.parent.find('a')['href']
        official.append({'name': name, 'category': "official", 'image_url': image_url, 'href': href})
    return official

officials = extract_restaurant_details(html_code)
print(f"Total number of official found: {len(officials)}")

# Write restaurant details to a JSON file
with open('officials.json', 'w') as json_file:
    json.dump(officials, json_file, indent=2)
# def extract_restaurant_details(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     pharmacy = []
#     for div in soup.find_all('div', class_='Nv2PK tH5CWc THOPZb'):
#         name = div.find('div', class_='qBF1Pd fontHeadlineSmall').text.strip()
#         # name = div.parent.find('a', class_='hfpxzc')['aria-label']
#         # image_url = div.find_next('img')['src']
#         # image_tag = div.find_next('img')
#         # image_url = image_tag['src'] if image_tag else None
#         # aria_label = div.parent.find('a', class_='hfpxzc')['aria-label']
#         href = div.parent.find('a')['href']
#         pharmacy.append({'name': name, 'category': "pharmacy", 'image_url': "image_url", 'href': href})
#     return pharmacy

# pharmacies = extract_restaurant_details(html_code)
# print(f"Total number of pharmacies found: {len(pharmacies)}")

# # Write restaurant details to a JSON file
# with open('pharmacies.json', 'w') as json_file:
#     json.dump(pharmacies, json_file, indent=2)