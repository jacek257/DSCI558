# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:05:25 2021

@author: Jimi
"""

from bs4 import BeautifulSoup as soup

html_doc = """<div id="main_top" class="main">


        <!-- feature announcement -->


    
    
    

        <!-- hero slot -->


    
    
    

    
	
	<!-- no content received for slot: provider_promotion -->
	



    
    
    


            <div class="title-overview">


  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleOverviewWidget_started');
    }
  </script>
        <div id="title-overview-widget" class="heroic-overview">
            <div class="vital">
      <div id="quicklinksBar" class="subnav">
  <div id="quicklinksMainSection">
         <a href="/title/tt2948372/fullcredits?ref_=tt_ql_1" class="quicklink">FULL CAST AND CREW</a> <span class="ghost">|</span>
         <a href="/title/tt2948372/trivia?ref_=tt_ql_2" class="quicklink">TRIVIA</a> <span class="ghost">|</span>
         <a href="/title/tt2948372/reviews?ref_=tt_ql_3" class="quicklink">USER REVIEWS</a> <span class="ghost">|</span>
      <a href="https://pro.imdb.com/title/tt2948372?rf=cons_tt_contact&amp;ref_=cons_tt_contact" class="quicklink">IMDbPro</a>
        <span class="ghost">|</span>
        <span class="show_more quicklink">
            MORE<span class="titleOverviewSprite quicklinksArrowUp"></span>
        </span>
        <span class="show_less quicklink" style="display:none">
           LESS<span class="titleOverviewSprite quicklinksArrowDown"></span>
        </span>
  </div>

    <span id="title-social-sharing-widget"><div class="dropdown share-widget"><button title="Share" class="quicklink"><span class="quicklink">SHARE</span></button><div class="dropdown-menu menu-right"><div class="dropdown-menu-item"><a href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt2948372%2F" title="Share on Facebook" windowwidth="626" windowheight="436" target="_blank"><span class="share-widget-sprite share facebook"></span>Facebook</a></div><div class="dropdown-menu-item"><a tweet="Soul (2020) - IMDb" href="http://twitter.com/intent/tweet?text=Soul%20(2020)%20-%20IMDb%20-%20https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt2948372%2F" title="Share on Twitter" windowwidth="815" windowheight="436" target="_blank"><span class="share-widget-sprite share twitter"></span>Twitter</a></div><div class="dropdown-menu-item"><a href="mailto:?subject=Check%20out%20this%20link%20on%20IMDb!&amp;body=Soul%20(2020)%20-%20IMDb - https://www.imdb.com/title/tt2948372/" title="Share by email"><span class="share-widget-sprite share email"></span>Email</a></div><div class="dropdown-menu-item"><div class="checkin-menu-item"><span class="open-checkin-popover"><span class="share-widget-sprite share checkin"></span>Check in</span></div></div><div class="dropdown-menu-item"><a href="https://www.imdb.com/title/tt2948372/" title="Click to copy"><span class="share-widget-copy-icon"><span class="share-widget-sprite share link"></span></span><div class="share-link-descriptor">Copy</div><div class="share-link-textbox"><input type="text" readonly="" value="https://www.imdb.com/title/tt2948372/"></div></a></div></div><div class="dropdown-overlay"></div></div></span>

        <div id="share-checkin">
<div class="add_to_checkins" data-const="tt2948372" data-lcn="title-maindetails">
<span class="btn2_wrapper"><a onclick="" class="btn2 large btn2_text_on checkins_action_btn"><span class="btn2_glyph">0</span><span class="btn2_text">Check in</span></a></span>    <div class="popup checkin-dialog" style="display: none;">
        <a class="dialog-close-button">X</a>
        <span class="title">I'm Watching This!</span>
        <div class="body">
            <div class="info">Keep track of everything you watch; tell your friends.
            </div>
            <div class="small message_box">
                <div class="hidden error" style="display: none;"><h2><div class="checkin-error">Error</div></h2> Please try again!</div>
                <div class="hidden success" style="display: none;"><h2><div class="checkin-success">Added to Your Check-Ins.</div></h2> <a href="/list/checkins">View</a></div>
            </div>
            <textarea data-msg="Enter a comment..." class="placeholder"></textarea>
            <div class="share">
                <button class="checkin-button"><span>Check in</span></button>
<!--
                    Check-ins are more fun when<br>
                    you <a href="/register/sharing">enable Facebook sharing</a>!
-->
            </div>
        </div>
    </div>
    <input type="hidden" name="49e6c" value="58b0">
</div>
        </div>

   <div class="quicklinkSection" id="full_subnav" style="display:none">           
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">DETAILS</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/fullcredits?ref_=tt_ql_dt_1" class="quicklink">Full Cast and Crew</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/releaseinfo?ref_=tt_ql_dt_2" class="quicklink">Release Dates</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/officialsites?ref_=tt_ql_dt_3" class="quicklink">Official Sites</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/companycredits?ref_=tt_ql_dt_4" class="quicklink">Company Credits</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/locations?ref_=tt_ql_dt_5" class="quicklink">Filming &amp; Production</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/technical?ref_=tt_ql_dt_6" class="quicklink">Technical Specs</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">STORYLINE</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/taglines?ref_=tt_ql_stry_1" class="quicklink">Taglines</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/plotsummary?ref_=tt_ql_stry_2" class="quicklink">Plot Summary</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/synopsis?ref_=tt_ql_stry_3" class="quicklink">Synopsis</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/keywords?ref_=tt_ql_stry_4" class="quicklink">Plot Keywords</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/parentalguide?ref_=tt_ql_stry_5" class="quicklink">Parents Guide</a>            </div>
    </div>
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">RELATED ITEMS</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/news?ref_=tt_ql_rel_1" class="quicklink">News</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/externalsites?ref_=tt_ql_rel_2" class="quicklink">External Sites</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">OPINION</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/awards?ref_=tt_ql_op_1" class="quicklink">Awards</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/faq?ref_=tt_ql_op_2" class="quicklink">FAQ</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/reviews?ref_=tt_ql_op_3" class="quicklink">User Reviews</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/ratings?ref_=tt_ql_op_4" class="quicklink">User Ratings</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/externalreviews?ref_=tt_ql_op_5" class="quicklink">External Reviews</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/criticreviews?ref_=tt_ql_op_6" class="quicklink">Metacritic Reviews</a>            </div>
    </div>
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">PHOTO &amp; VIDEO</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/mediaindex?ref_=tt_ql_pv_1" class="quicklink">Photo Gallery</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/videogallery?ref_=tt_ql_pv_2" class="quicklink">Trailers and Videos</a>            </div>
    </div>
               </div>
               <div class="quicklinkSectionColumn">
    <div class="quicklinkGroup">
        <div class="quicklinkSectionHeader">DID YOU KNOW?</div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/trivia?ref_=tt_ql_trv_1" class="quicklink">Trivia</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/goofs?ref_=tt_ql_trv_2" class="quicklink">Goofs</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/crazycredits?ref_=tt_ql_trv_3" class="quicklink">Crazy Credits</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/quotes?ref_=tt_ql_trv_4" class="quicklink">Quotes</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/alternateversions?ref_=tt_ql_trv_5" class="quicklink quicklinkGray">Alternate Versions</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/movieconnections?ref_=tt_ql_trv_6" class="quicklink">Connections</a>            </div>
            <div class="quicklinkSectionItem">
<a href="/title/tt2948372/soundtrack?ref_=tt_ql_trv_7" class="quicklink">Soundtracks</a>            </div>
    </div>
               </div>
   </div>
      </div>  

                <div class="title_block">
                    <div class="title_bar_wrapper">

    <div class="ratings_wrapper">
            <div class="imdbRating" itemtype="http://schema.org/AggregateRating" itemscope="" itemprop="aggregateRating">
                    <div class="ratingValue">
<strong title="8.1 based on 154,843 user ratings"><span itemprop="ratingValue">8.1</span></strong><span class="grey">/</span><span class="grey" itemprop="bestRating">10</span>                    </div>
                    <a href="/title/tt2948372/ratings?ref_=tt_ov_rt"><span class="small" itemprop="ratingCount">154,843</span></a>
                        <div class="hiddenImportant">
                                <span itemprop="reviewCount">1,359 user</span>
                                <span itemprop="reviewCount">277 critic</span>
                        </div>
            </div>

  <div id="star-rating-widget" class="star-rating-widget" data-tconst="tt2948372" data-rating="0" data-user="" data-auth="" data-tracking-tag="title-maindetails" data-rating-share-enabled="false" data-title="Soul" data-rating-next-share-time="2000-01-01T00:00:00.000Z" data-rating-share-treatment="C"><div class="star-rating-button"><button><span class="star-rating-star no-rating"></span><span class="star-rating-text">Rate This</span></button><div value="0" ratetext="Rate This" ratesubtext="You" class="star-rating"><span><a class="star-rating-delete" title="Delete" rel="nofollow"></a><span class="star-rating-stars"><a class="" title="Click to rate: 1" rel="nofollow"><span>1</span></a><a class="" title="Click to rate: 2" rel="nofollow"><span>2</span></a><a class="" title="Click to rate: 3" rel="nofollow"><span>3</span></a><a class="" title="Click to rate: 4" rel="nofollow"><span>4</span></a><a class="" title="Click to rate: 5" rel="nofollow"><span>5</span></a><a class="" title="Click to rate: 6" rel="nofollow"><span>6</span></a><a class="" title="Click to rate: 7" rel="nofollow"><span>7</span></a><a class="" title="Click to rate: 8" rel="nofollow"><span>8</span></a><a class="" title="Click to rate: 9" rel="nofollow"><span>9</span></a><a class="" title="Click to rate: 10" rel="nofollow"><span>10</span></a></span></span><span class="star-rating-value">0</span></div></div></div>
    </div>
    <div class="titleBar">
        <div class="primary_ribbon">
            <div class="ribbonize" data-tconst="tt2948372" data-caller-name="title" style="position: relative;"><div class="wl-ribbon standalone not-inWL" title="Click to add to watchlist"></div></div>
            <div class="wlb_dropdown_btn btn2_wrapper btn2_active wlb_dropdown" data-tconst="tt2948372" data-size="large" data-caller-name="title" data-type="primary" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 large primary btn2_glyph_on" onclick=""><span class="btn2_glyph"><div class="btn2_down"></div></span><span class="btn2_text"></span></a></div>
            <div class="wlb_dropdown_list" style="display:none"></div>
        </div>

        <div class="title_wrapper">
<h1 class="">Soul&nbsp;<span id="titleYear">(<a href="/year/2020/?ref_=tt_ov_inf">2020</a>)</span>            </h1>
            <div class="subtext">
                    PG
    <span class="ghost">|</span>                    <time datetime="PT100M">
                        1h 40min
                    </time>
    <span class="ghost">|</span>
<a href="/search/title?genres=animation&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Animation</a>, 
<a href="/search/title?genres=adventure&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Adventure</a>, 
<a href="/search/title?genres=comedy&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Comedy</a>
    <span class="ghost">|</span>
<a href="/title/tt2948372/releaseinfo?ref_=tt_ov_inf" title="See more release dates">25 December 2020 (USA)
</a>            </div>
        </div>
    </div>
                    </div>
                </div>




                    <div class="slate_wrapper">
    <div class="poster">
<a href="/title/tt2948372/mediaviewer/rm4113422337?ref_=tt_ov_i"> <img alt="Soul Poster" title="Soul Poster" src="https://m.media-amazon.com/images/M/MV5BZGE1MDg5M2MtNTkyZS00MTY5LTg1YzUtZTlhZmM1Y2EwNmFmXkEyXkFqcGdeQXVyNjA3OTI0MDc@._V1_UX182_CR0,0,182,268_AL_.jpg">
</a>    </div>
                        <!--Begin inline video hero weblab check-->
    <div class="slate">
<a href="/video/imdb/vi1257423129?playlistId=tt2948372&amp;ref_=tt_ov_vi" class="slate_button prevent-ad-overlay video-modal" data-type="recommends" data-tconst="tt2948372" data-video="vi1257423129" data-context="imdb" data-refsuffix="tt_ov_vi" data-pixels=""> <img alt="Trailer" title="Trailer" src="https://m.media-amazon.com/images/M/MV5BNTM1OWExMmYtZWFhNS00YWU1LTkxMTQtMTAzZDgyNzFmYTVmXkEyXkFqcGdeQWpnYW1i._V1_UX477_CR0,0,477,268_AL_.jpg">
<div class="slate_fade_top"></div>
<div class="slate_fade_bottom"></div>
</a>        <div class="caption">
            <div style="float: left;">2:24 <span class="ghost">|</span> Trailer</div>
                <div style="float: right;">        <a href="/title/tt2948372/videogallery?ref_=tt_ov_vi_sm">23 VIDEOS</a>
    <span class="ghost">|</span>        <a href="/title/tt2948372/mediaindex?ref_=tt_ov_mi_sm">58 IMAGES</a>
</div>
            <div style="clear: both;"></div>
        </div>
    </div>
                    </div>
            </div>
        <script type="text/javascript">
            window.IMDbLocalizedPlots = { titleId: "tt2948372", t1:false, t2:true };
        </script>
    <div class="plot_summary_wrapper localized">
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitlePlotAndCreditSummaryWidget_started');
    }
  </script>
    <div class="plot_summary ">
            <div class="summary_text ready"><div class="localized-plot "><div class="plot-text"><div class="ipc-html-content ipc-html-content--base"><div>
                    After landing the gig of a lifetime, a New York jazz pianist suddenly finds himself trapped in a strange land between Earth and the afterlife.
            </div></div></div><div class="locale-select"><div class="locale-label"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" class="ipc-icon ipc-icon--language" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2s.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2s.07-1.35.16-2h4.68c.09.65.16 1.32.16 2s-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2s-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"></path></svg> EN<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--arrow-drop-down" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M8.71 11.71l2.59 2.59c.39.39 1.02.39 1.41 0l2.59-2.59c.63-.63.18-1.71-.71-1.71H9.41c-.89 0-1.33 1.08-.7 1.71z"></path></svg></div></div></div></div>

    <div class="credit_summary_item">
        <h4 class="inline">Directors:</h4>
<a href="/name/nm0230032/?ref_=tt_ov_dr">Pete Docter</a>, <a href="/name/nm5358492/?ref_=tt_ov_dr">Kemp Powers</a> (co-director)    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Writers:</h4>
<a href="/name/nm0230032/?ref_=tt_ov_wr">Pete Docter</a> (story &amp; screenplay by), <a href="/name/nm0428873/?ref_=tt_ov_wr">Mike Jones</a> (story &amp; screenplay by)            <span class="ghost">|</span>
<a href="fullcredits?ref_=tt_ov_wr#writers/">1 more credit</a>&nbsp;»
    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Stars:</h4>
<a href="/name/nm0004937/?ref_=tt_ov_st_sm">Jamie Foxx</a>, <a href="/name/nm0275486/?ref_=tt_ov_st_sm">Tina Fey</a>, <a href="/name/nm0636218/?ref_=tt_ov_st_sm">Graham Norton</a>            <span class="ghost">|</span>
<a href="fullcredits/?ref_=tt_ov_st_sm">See full cast &amp; crew</a>&nbsp;»
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitlePlotAndCreditSummaryWidget_finished');
    }
  </script>
        <!--To display Pro Title CTA above the watchlist for in-development titles -->

    <div class="uc-add-wl-button uc-add-wl--not-in-wl uc-add-wl" data-title-id="tt2948372" data-is-logged-in="false" data-is-watchlisted="false" title="Click to add to watchlist" data-widget-type="wl_button" data-ref-tag-prefix="tt_ov" data-record-metric="true" data-uc-add-wl="">
        






        <button class="ipc-button uc-add-wl-button-icon--done watchlist--title-main-desktop-standalone ipc-button--core-base ipc-button--single-padding ipc-button--default-height">


<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--done  ipc-button__icon ipc-button__icon--pre" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M9 16.2l-3.5-3.5a.984.984 0 0 0-1.4 0 .984.984 0 0 0 0 1.4l4.19 4.19c.39.39 1.02.39 1.41 0L20.3 7.7a.984.984 0 0 0 0-1.4.984.984 0 0 0-1.4 0L9 16.2z"></path></svg>    <div class="ipc-button__text">Added to Watchlist</div>
        </button>

        






        <button class="ipc-button uc-add-wl-button-icon--add watchlist--title-main-desktop-standalone ipc-button--core-base ipc-button--single-padding ipc-button--default-height">


<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="ipc-icon ipc-icon--add  ipc-button__icon ipc-button__icon--pre" viewBox="0 0 24 24" fill="currentColor" role="presentation"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M18 13h-5v5c0 .55-.45 1-1 1s-1-.45-1-1v-5H6c-.55 0-1-.45-1-1s.45-1 1-1h5V6c0-.55.45-1 1-1s1 .45 1 1v5h5c.55 0 1 .45 1 1s-.45 1-1 1z"></path></svg>    <div class="ipc-button__text">Add to Watchlist</div>
        </button>

            <div class="uc-add-wl-pending-icon"></div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleReviewsAndPopularityWidget_started');
    }
  </script>
      <div class="titleReviewBar ">           
    <div class="titleReviewBarItem">
<a href="criticreviews?ref_=tt_ov_rt"> <div class="metacriticScore score_favorable titleReviewBarSubItem">
<span>83</span>
</div></a>        <div class="titleReviewBarSubItem">
            <div><a href="criticreviews?ref_=tt_ov_rt">
Metascore
</a>            </div>
            <div><span class="subText"> 
               From <a href="http://www.metacritic.com" target="_blank">metacritic.com</a> 
               </span>
            </div>
        </div>
    </div>
                   <div class="divider"></div>
           
    <div class="titleReviewBarItem titleReviewbarItemBorder">
        <div>
        Reviews
        </div>
        <div>
            <span class="subText">
                   <a href="reviews?ref_=tt_ov_rt">1,359 user</a>                   
                       <span class="ghostText">|</span>
                   <a href="externalreviews?ref_=tt_ov_rt">277 critic</a>
             </span>
        </div>
    </div>
                   <div class="divider"></div>

    <div class="titleReviewBarItem">
  <div class="titleOverviewSprite popularityTrendDown"></div>
        <div class="titleReviewBarSubItem">
            <div>
            Popularity
            </div>
            <div>
                <span class="subText">
                    5
      (<span class="titleOverviewSprite popularityImageDown"></span> <span class="popularityDown">3</span>)
                </span>
            </div>
        </div>                                   
    </div>
      </div>              
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleReviewsAndPopularityWidget_finished');
    }
  </script>
    </div>
                <!--To display Pro Title CTA below the review bar for completed titles -->

            <div class="pro_logo_main_title">
    <div id="title_completed_pro_link" class="pro_title_link_with_separator">
<a href="https://pro.imdb.com/title/tt2948372?rf=cons_tt_atf&amp;ref_=cons_tt_atf" class="pro_title_href"> <img src="https://m.media-amazon.com/images/S/sash/u4ZG4O9Kh-h0yDb.png" class="pro_logo">
<span class="pro_title_link_text">
View production, box office, &amp; company info
</span>
<img src="https://m.media-amazon.com/images/S/sash/mGkoj7mMfYpKOdk.png" class="pro_link_icon">
</a>    </div>
            </div>
        </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleOverviewWidget_finished');
    }
  </script>
            </div>

<script>
    if (typeof uet == 'function') {
      uet("af");
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_atf_main');
    }
  </script>

    </div>"""
    
html2 = """<div id="main_bottom" class="main">

        




<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleAwardsWidget", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsWidget_started');
      }
    </script>
      <div class="article highlighted" id="titleAwardsRanks">
          <strong>
<a href="/chart/top?ref_=tt_awd"> Top Rated Movies #202
</a>          </strong>
          |

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsSummaryWidget_started');
      }
    </script>
    <span class="awards-blurb">
        45 wins &amp; 29 nominations.
    </span>
            <span class="see-more inline">
<a href="/title/tt2948372/awards?ref_=tt_awd" class="btn-full">See more awards</a>&nbsp;»            </span>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsSummaryWidget_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleAwardsSummaryWidget", {wb: 1});
    }
</script>
      </div>
    <script>
      if ('csm' in window) {
        csm.measure('csm_TitleAwardsWidget_finished');
      }
    </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleAwardsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleAwardsWidget", {wb: 1});
    }
</script>


<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleMediaStripWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleMediaStripWidget_started');
    }
  </script>
        <div class="article" id="titleVideoStrip">
            <h2>Videos</h2>
    <div class="mediastrip_big">
                <span class="video_slate">

<a href="/title/tt2948372/videoplayer/vi1257423129?ref_=tt_pv_vi_aiv_1" class="video-modal" data-video="vi1257423129" data-context="imdb" data-rid="AH2X689XMC4TG44TAZGF" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/M/MV5BNTM1OWExMmYtZWFhNS00YWU1LTkxMTQtMTAzZDgyNzFmYTVmXkEyXkFqcGdeQWpnYW1i._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZATrailer,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA02%253A24,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZASoul,24,138,14,176,arialbd,7,255,255,255,1_.jpg" class="loadlate video" viconst="vi1257423129"></a>            </span>
                <span class="video_slate">

<a href="/title/tt2948372/videoplayer/vi1645723161?ref_=tt_pv_vi_aiv_2" class="video-modal" data-video="vi1645723161" data-context="imdb" data-rid="AH2X689XMC4TG44TAZGF" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/M/MV5BYzNlOTRhY2MtNmE0Zi00ZGE3LTg0NGQtNzczNjBlMDNhYzcxXkEyXkFqcGdeQWFybm8@._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZATrailer,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA01%253A01,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZASoul,24,138,14,176,arialbd,7,255,255,255,1_.jpg" class="loadlate video" viconst="vi1645723161"></a>            </span>
                <span class="video_slate_last">

<a href="/title/tt2948372/videoplayer/vi2544680473?ref_=tt_pv_vi_aiv_3" class="video-modal" data-video="vi2544680473" data-context="imdb" data-rid="AH2X689XMC4TG44TAZGF" widget-context="titleMainDetails"><img height="" width="" alt="" title="" src="https://m.media-amazon.com/images/M/MV5BN2Y1YTU1YTctNDVmNC00NzhiLWFmNjctYzkxNDliMDViYzVlXkEyXkFqcGdeQWpnYW1i._V1_SP330,330,0,C,0,0,0_CR65,90,200,150_PIimdb-blackband-204-14,TopLeft,0,0_PIimdb-blackband-204-28,BottomLeft,0,1_CR0,0,200,150_PIimdb-bluebutton-big,BottomRight,-1,-1_ZATrailer,4,123,16,196,verdenab,8,255,255,255,1_ZAon%2520IMDb,4,1,14,196,verdenab,7,255,255,255,1_ZA02%253A20,164,1,14,36,verdenab,7,255,255,255,1_PIimdb-HDIconMiniWhite,BottomLeft,4,-2_ZASoul,24,138,14,176,arialbd,7,255,255,255,1_.jpg" class="loadlate video" viconst="vi2544680473"></a>            </span>
    </div>
            <div class="combined-see-more see-more">
<a href="/title/tt2948372/videogallery?ref_=tt_pv_vi_sm"> See all 23 videos
</a>&nbsp;»
            </div>
        </div>



            <div class="article" id="titleImageStrip">
                <h2>Photos</h2>
    <div class="mediastrip">        	
                
<a href="/title/tt2948372/mediaviewer/rm1227002113?context=default&amp;ref_=tt_pv_md_1"><img height="99" width="99" alt="Tina Fey and Questlove at an event for Soul (2020)" title="Tina Fey and Questlove at an event for Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BZjk4YzNjMjQtNzNmMy00ZWI5LTk2OWMtYjVmMWRiMjVkMDE5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UY99_CR14,0,99,99_AL_.jpg" class="loadlate"></a>                
<a href="/title/tt2948372/mediaviewer/rm3627323649?context=default&amp;ref_=tt_pv_md_2"><img height="99" width="99" alt="Tina Fey in Soul (2020)" title="Tina Fey in Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BYjMwYjkxNjMtZjkyMS00NmQ5LWI5ZDgtYjZjMjg4OGMyNjMwXkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_UY99_CR69,0,99,99_AL_.jpg" class="loadlate"></a>                
<a href="/title/tt2948372/mediaviewer/rm1092784385?context=default&amp;ref_=tt_pv_md_3"><img height="99" width="99" alt="Questlove at an event for Soul (2020)" title="Questlove at an event for Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BMmY1ZmY4MDctNzYxYy00NDc2LWE5MTctZDE1OGVmMTdkODFjXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX99_CR0,0,99,99_AL_.jpg" class="loadlate"></a>                
<a href="/title/tt2948372/mediaviewer/rm3950760193?context=default&amp;ref_=tt_pv_md_4"><img height="99" width="99" alt="Soul (2020)" title="Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BY2EyYWI4MGQtNTA5YS00MTE3LTk5ODUtYzllMWI3YmRmMzFmXkEyXkFqcGdeQXVyMTI1MDE2Mzky._V1_UY99_CR77,0,99,99_AL_.jpg" class="loadlate"></a>                
<a href="/title/tt2948372/mediaviewer/rm540381441?context=default&amp;ref_=tt_pv_md_5"><img height="99" width="99" alt="Jamie Foxx in Soul (2020)" title="Jamie Foxx in Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BNDIyYzZkNDQtMGVlYS00OWI5LWI3YmEtNjQ0NGFkZmJlODk2XkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_UY99_CR69,0,99,99_AL_.jpg" class="loadlate"></a>                
<a href="/title/tt2948372/mediaviewer/rm3418741249?context=default&amp;ref_=tt_pv_md_6"><img height="99" width="99" alt="Soul (2020)" title="Soul (2020)" src="https://m.media-amazon.com/images/M/MV5BZmJlNGFkZWMtNmVmMS00MjIxLWI2NzMtOWM4NDZlMjM4Mjg2XkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UY99_CR68,0,99,99_AL_.jpg" class="loadlate"></a>    </div>
                    <div class="combined-see-more see-more">
<a href="/title/tt2948372/mediaindex?ref_=tt_pv_mi_sm"><span class="titlePageSprite showAllVidsAndPics"></span></a>
<a href="/title/tt2948372/mediaindex?ref_=tt_pv_mi_sm"> See all
58 photos</a>&nbsp;»                    </div>
            </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleMediaStripWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleMediaStripWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleMediaStripWidget", {wb: 1});
    }
</script>

        <!-- cast list -->

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleCastWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleCastWidget_started');
    }
  </script>
    <div class="article" id="titleCast">
    <span class="rightcornerlink">
            <a href="/register/login?why=edit&amp;ref_=tt_cl" rel="login">Edit</a>
    </span>
        <h2>Cast</h2>
        
        <table class="cast_list">    
  <tbody><tr><td colspan="4" class="castlist_label">Cast overview, first billed only:</td></tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0004937/?ref_=tt_cl_i1"><img height="44" width="32" alt="Jamie Foxx" title="Jamie Foxx" src="https://m.media-amazon.com/images/M/MV5BMTkyNjY1NDg3NF5BMl5BanBnXkFtZTgwNjA2MTg0MzE@._V1_UY44_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0004937/?ref_=tt_cl_t1"> Jamie Foxx
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0004937?ref_=tt_cl_t1">Joe</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0275486/?ref_=tt_cl_i2"><img height="44" width="32" alt="Tina Fey" title="Tina Fey" src="https://m.media-amazon.com/images/M/MV5BZTE1YTgzYzctNDgyYS00OTY5LThmYjItZGQ2ZjJmY2NhY2I3XkEyXkFqcGdeQXVyMTAwOTg0NzU5._V1_UY44_CR23,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0275486/?ref_=tt_cl_t2"> Tina Fey
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0275486?ref_=tt_cl_t2">22</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0636218/?ref_=tt_cl_i3"><img height="44" width="32" alt="Graham Norton" title="Graham Norton" src="https://m.media-amazon.com/images/M/MV5BOTI0MTkzMzgwMF5BMl5BanBnXkFtZTYwNTYyMTA1._V1_UY44_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0636218/?ref_=tt_cl_t3"> Graham Norton
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0636218?ref_=tt_cl_t3">Moonwind</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1344302/?ref_=tt_cl_i4"><img height="44" width="32" alt="Rachel House" title="Rachel House" src="https://m.media-amazon.com/images/M/MV5BMWNmNzEzMGUtMDc1NS00OTlkLWExMzktNTAzOGQ2N2RkMjI3XkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1344302/?ref_=tt_cl_t4"> Rachel House
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm1344302?ref_=tt_cl_t4">Terry</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0103797/?ref_=tt_cl_i5"><img height="44" width="32" alt="Alice Braga" title="Alice Braga" src="https://m.media-amazon.com/images/M/MV5BMTgwNjE4NzU4M15BMl5BanBnXkFtZTcwMDQ5NDI2MQ@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0103797/?ref_=tt_cl_t5"> Alice Braga
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0103797?ref_=tt_cl_t5">Counselor Jerry</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1547964/?ref_=tt_cl_i6"><img height="44" width="32" alt="Richard Ayoade" title="Richard Ayoade" src="https://m.media-amazon.com/images/M/MV5BMjE0MDIzMDM4Nl5BMl5BanBnXkFtZTcwODc4MzczNA@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1547964/?ref_=tt_cl_t6"> Richard Ayoade
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm1547964?ref_=tt_cl_t6">Counselor Jerry</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0711118/?ref_=tt_cl_i7"><img height="44" width="32" alt="Phylicia Rashad" title="Phylicia Rashad" src="https://m.media-amazon.com/images/M/MV5BMTczMzcxNzYyN15BMl5BanBnXkFtZTcwMTAyMDQ2NA@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0711118/?ref_=tt_cl_t7"> Phylicia Rashad
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0711118?ref_=tt_cl_t7">Libba</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0712603/?ref_=tt_cl_i8"><img height="44" width="32" alt="Donnell Rawlings" title="Donnell Rawlings" src="https://m.media-amazon.com/images/M/MV5BMTYwNDI3NzYzN15BMl5BanBnXkFtZTcwMjU1NzYxOA@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0712603/?ref_=tt_cl_t8"> Donnell Rawlings
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0712603?ref_=tt_cl_t8">Dez</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0859821/?ref_=tt_cl_i9"><img height="44" width="32" alt="Questlove" title="Questlove" src="https://m.media-amazon.com/images/M/MV5BMTU5OTA0OTI5NV5BMl5BanBnXkFtZTYwMjU3OTI4._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0859821/?ref_=tt_cl_t9"> Questlove
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0859821?ref_=tt_cl_t9">Curley</a> 
  
  
  (voice) (as Ahmir-Khalib Thompson a.k.a. Questlove)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000291/?ref_=tt_cl_i10"><img height="44" width="32" alt="Angela Bassett" title="Angela Bassett" src="https://m.media-amazon.com/images/M/MV5BMjI4OTQ1NTcxOF5BMl5BanBnXkFtZTcwOTc1NTU0OQ@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0000291/?ref_=tt_cl_t10"> Angela Bassett
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0000291?ref_=tt_cl_t10">Dorothea</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm11973242/?ref_=tt_cl_i11"><img height="44" width="32" alt="Cora Champommier" title="Cora Champommier" src="https://m.media-amazon.com/images/M/MV5BYTk5YTZlMTQtODk2MS00MGM4LWFiZWUtYTNiZGY5ODA0NzI1XkEyXkFqcGdeQXVyNTI5NjMyNjc@._V1_UY44_CR3,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm11973242/?ref_=tt_cl_t11"> Cora Champommier
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm11973242?ref_=tt_cl_t11">Connie</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0355863/?ref_=tt_cl_i12"><img height="44" width="32" alt="Margo Hall" title="Margo Hall" src="https://m.media-amazon.com/images/M/MV5BMjYwZWJjNGYtN2M5OC00ZGFiLTk0NzItZTIyMTYwYTJiMmNhXkEyXkFqcGdeQXVyODkxNzEzMjI@._V1_UY44_CR17,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0355863/?ref_=tt_cl_t12"> Margo Hall
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0355863?ref_=tt_cl_t12">Melba</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4377526/?ref_=tt_cl_i13"><img height="44" width="32" alt="Daveed Diggs" title="Daveed Diggs" src="https://m.media-amazon.com/images/M/MV5BMTY5NzA2ODI1MV5BMl5BanBnXkFtZTgwMzg1OTg4ODE@._V1_UY44_CR7,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm4377526/?ref_=tt_cl_t13"> Daveed Diggs
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm4377526?ref_=tt_cl_t13">Paul</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1159336/?ref_=tt_cl_i14"><img height="44" width="32" alt="Rhodessa Jones" title="Rhodessa Jones" src="https://m.media-amazon.com/images/S/sash/N1QWYSqAfSJV62Y.png" class=""></a>          </td>
          <td>
<a href="/name/nm1159336/?ref_=tt_cl_t14"> Rhodessa Jones
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm1159336?ref_=tt_cl_t14">Lulu</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0836071/?ref_=tt_cl_i15"><img height="44" width="32" alt="Wes Studi" title="Wes Studi" src="https://m.media-amazon.com/images/M/MV5BMTkyODcyMzgwNl5BMl5BanBnXkFtZTcwMjIzNTUyMQ@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0836071/?ref_=tt_cl_t15"> Wes Studi
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt2948372/characters/nm0836071?ref_=tt_cl_t15">Counselor Jerry</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
        </tbody></table>
        <div class="see-more">
            <a href="fullcredits?ref_=tt_cl_sm#cast">See full cast</a>&nbsp;»
        </div>
        <div class="pro_logo_main_title">
    <div id="cast_title_pro_link" class="pro_title_cast_link">
<a href="https://pro.imdb.com/title/tt2948372?rf=cons_tt_btf_cc&amp;ref_=cons_tt_btf_cc" class="pro_title_href"> <img src="https://m.media-amazon.com/images/S/sash/UXH1lealHjWQtLQ.png" class="pro_logo">
<span class="pro_title_link_text">
View production, box office, &amp; company info
</span>
<img src="https://m.media-amazon.com/images/S/sash/mGkoj7mMfYpKOdk.png" class="pro_link_icon">
</a>    </div>
        </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleCastWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleCastWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleCastWidget", {wb: 1});
    }
</script>



    
    
        <a name="slot_center-3"></a>
        <div class="article">
        
    
        
                                

    
            <script type="text/javascript">if(typeof uet === 'function'){uet('bb','NinjaWidget',{wb:1});}</script>
                                

                    
    
        <span class="ab_widget">
        
    

    <div class="ab_ninja">
<span class="widget_header"> <span class="oneline"> <a href="/list/ls025720609/videoplayer/vi1527955737?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_hd"> <h3> 'Soul' Cast Share Life Lessons From Their Characters</h3> </a> </span> </span> <div class="widget_content no_inline_blurb"> <div class="widget_nested"> <div class="ninja_image_pack"> <div class="ninja_center"> <div class="ninja_image first_image last_image" style="width:624px;height:auto;"> <div style="width:624px;height:auto;margin:0 auto;"> <div class="widget_image"> <div class="image"> <a href="/list/ls025720609/videoplayer/vi1527955737?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_i_1" class="video-modal" data-refsuffix="tt_ots_soul_jkt2" data-ref="tt_ots_soul_jkt2_i_1"> <img class="pri_image" title="IMDb on the Scene - Interviews (2017-)" alt="IMDb on the Scene - Interviews (2017-)" src="https://m.media-amazon.com/images/M/MV5BNTUzZjhkYTktMzQzZi00NWY2LWFkYmItZWIyM2U4OWFhNTE4XkEyXkFqcGdeQXRyYW5zY29kZS13b3JrZmxvdw@@._CR192,147,1404,790._SY351_SX624_AL_.jpg"> <img alt="IMDb on the Scene - Interviews (2017-)" title="IMDb on the Scene - Interviews (2017-)" class="image_overlay overlay_mouseout" src="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button._CB485946531_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button._CB485946531_.png"> <img alt="IMDb on the Scene - Interviews (2017-)" title="IMDb on the Scene - Interviews (2017-)" class="image_overlay overlay_mouseover" src="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button-hover._CB485934747_.png" data-src-x2="https://m.media-amazon.com/images/G/01/IMDb/icon/play-button-hover._CB485934747_.png"> </a> </div> </div> </div> </div> </div> </div> </div> </div> <p class="blurb"><i><a href="/title/tt2948372?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk1">Soul</a></i> stars <a href="/name/nm0004937?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk2">Jamie Foxx</a>, <a href="/name/nm0275486?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk3">Tina Fey</a>, <a href="/name/nm0000291?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk4">Angela Bassett</a>, <a href="/name/nm0711118?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk5">Phylicia Rashad</a>, and <a href="/name/nm0859821?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_lk6">Questlove</a> share the most memorable things they learned from portraying their characters in Pixar's latest movie.</p> <p class="seemore"><a href="/list/ls025720609/videoplayer/vi1527955737?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=905808fb-ecaa-4ace-98a4-5f927b08bb18&amp;pf_rd_r=AH2X689XMC4TG44TAZGF&amp;pf_rd_s=center-3&amp;pf_rd_t=15021&amp;pf_rd_i=tt2948372&amp;ref_=tt_ots_soul_jkt2_sm" class="position_bottom supplemental"> Watch now</a></p>    </div>
    

                        
        </span>



            <script type="text/javascript">
                if(typeof uex === 'function'){uex('ld','NinjaWidget',{wb:1});}
            </script>
        




        </div>
    



    
    
    



    
    
    


<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleRecsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleRecsWidget_started');
    }
  </script>


                <div class="article" id="titleRecs">
                                 <span class="rightcornerlink">
             <a href="https://help.imdb.com/article/imdb/discover-watch/what-is-the-more-like-this-section/GPE7SPGZREKKY7YN?ref_=cons_tt_rec_lm">Learn more</a>
             </span>

             <h2 class="rec_heading_wrapper">
                     <span class="rec_heading" data-spec="p13nsims:tt2948372" style="">More Like This&nbsp;</span>
             </h2>

                        <div class="rec_wrapper" id="title_recs" data-items-per-request="24" data-items-per-page="6" data-specs="p13nsims:tt2948372" data-caller-name="p13nsims-title" data-type="sims">

    <div class="rec_const_picker">
        <div class="rec_view">
            <div class="rec_grave" style="display:none"></div>
            <div class="rec_slide" style="width: 492px;">
                        <div class="rec_page rec_selected">         
    
    
    <div class="rec_item rec_selected" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt2380307">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt2380307/?ref_=tt_sims_tti"><img height="113" width="76" alt="Coco" title="Coco" src="https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY113_CR1,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt2096673">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt2096673/?ref_=tt_sims_tti"><img height="113" width="76" alt="Inside Out" title="Inside Out" src="https://m.media-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0087538">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0087538/?ref_=tt_sims_tti"><img height="113" width="76" alt="The Karate Kid" title="The Karate Kid" src="https://m.media-amazon.com/images/M/MV5BNTkzY2YzNmYtY2ViMS00MThiLWFlYTEtOWQ1OTBiOGEwMTdhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX76_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4566758">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4566758/?ref_=tt_sims_tti"><img height="113" width="76" alt="Mulan" title="Mulan" src="https://m.media-amazon.com/images/M/MV5BNDliY2E1MjUtNzZkOS00MzJlLTgyOGEtZDg4MTI1NzZkMTBhXkEyXkFqcGdeQXVyNjMwMzc3MjE@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4729430">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4729430/?ref_=tt_sims_tti"><img height="113" width="76" alt="Klaus" title="Klaus" src="https://m.media-amazon.com/images/M/MV5BMWYwOThjM2ItZGYxNy00NTQwLWFlZWEtM2MzM2Q5MmY3NDU5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt1049413">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt1049413/?ref_=tt_sims_tti"><img height="113" width="76" alt="Up" title="Up" src="https://m.media-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX76_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

                        </div>
                        <div class="rec_page">         
    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt7146812">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt7146812/?ref_=tt_sims_tti"><img height="113" width="76" alt="Onward" title="Onward" src="https://m.media-amazon.com/images/M/MV5BMTZlYzk3NzQtMmViYS00YWZmLTk5ZTEtNWE0NGVjM2MzYWU1XkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0198781">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0198781/?ref_=tt_sims_tti"><img height="113" width="76" alt="Monsters, Inc." title="Monsters, Inc." src="https://m.media-amazon.com/images/M/MV5BMTY1NTI0ODUyOF5BMl5BanBnXkFtZTgwNTEyNjQ0MDE@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0910970">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0910970/?ref_=tt_sims_tti"><img height="113" width="76" alt="WALL·E" title="WALL·E" src="https://m.media-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4633694">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4633694/?ref_=tt_sims_tti"><img height="113" width="76" alt="Spider-Man: Into the Spider-Verse" title="Spider-Man: Into the Spider-Verse" src="https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0266543">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0266543/?ref_=tt_sims_tti"><img height="113" width="76" alt="Finding Nemo" title="Finding Nemo" src="https://m.media-amazon.com/images/M/MV5BZTAzNWZlNmUtZDEzYi00ZjA5LWIwYjEtZGM1NWE1MjE4YWRhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX76_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

    
    
    <div class="rec_item" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0110357">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0110357/?ref_=tt_sims_tti"><img height="113" width="76" alt="The Lion King" title="The Lion King" src="https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UY113_CR0,0,76,113_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>

                        </div>
            </div>
            <div class="rec_nav">
                <div class="rec_nav_page_num"></div>
                <a class="rec_nav_left rec_nav_disabled">◄ Prev 6</a>
                <a class="rec_nav_right">Next 6 ►</a>
            </div>
        </div>
    </div>

   <div class="rec_overviews">


      <div class="rec_overview" data-tconst="tt2380307" style="">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt2380307">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt2380307/?ref_=tt_sims_tti"><img height="190" width="128" alt="Coco" title="Coco" src="https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGdeQXVyODIxMzk5NjA@._V1_UY190_CR2,0,128,190_AL_.jpg" class="loadlate rec_poster_img"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt2380307" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt2380307/?ref_=tt_sims_tt"><b>Coco</b></a>
        <span>I</span>
            <span class="nobr">(2017)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Coco (2017)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Family


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt2380307|imdb|8.4|8.4|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.4/10 (383,504 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 117.6px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Lee Unkrich,
Adrian Molina  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Anthony Gonzalez,
Gael García Bernal,
Benjamin Bratt</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt2096673" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt2096673">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt2096673/?ref_=tt_sims_tti"><img height="190" width="128" alt="Inside Out" title="Inside Out" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt2096673" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt2096673/?ref_=tt_sims_tt"><b>Inside Out</b></a>
        <span>I</span>
            <span class="nobr">(2015)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Inside Out (2015)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt2096673|imdb|8.1|8.1|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.1/10 (615,752 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 113.4px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.1</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Pete Docter,
Ronnie Del Carmen  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Amy Poehler,
Bill Hader,
Lewis Black</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0087538" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0087538">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0087538/?ref_=tt_sims_tti"><img height="190" width="128" alt="The Karate Kid" title="The Karate Kid" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNTkzY2YzNmYtY2ViMS00MThiLWFlYTEtOWQ1OTBiOGEwMTdhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX128_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt0087538" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0087538/?ref_=tt_sims_tt"><b>The Karate Kid</b></a>
            <span class="nobr">(1984)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for The Karate Kid (1984)" class="us_pg titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span> 
                     Drama
     <span class="ghost">|</span> 
                     Family


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0087538|imdb|7.3|7.3|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 7.3/10 (195,506 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 102.2px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">7.3</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    A martial arts master agrees to teach karate to a bullied teenager.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
John G. Avildsen  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Ralph Macchio,
Pat Morita,
Elisabeth Shue</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt4566758" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4566758">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4566758/?ref_=tt_sims_tti"><img height="190" width="128" alt="Mulan" title="Mulan" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BNDliY2E1MjUtNzZkOS00MzJlLTgyOGEtZDg4MTI1NzZkMTBhXkEyXkFqcGdeQXVyNjMwMzc3MjE@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt4566758" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt4566758/?ref_=tt_sims_tt"><b>Mulan</b></a>
            <span class="nobr">(2020)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Mulan (2020)" class="us_pg_13 titlePageSprite absmiddle"></span>

                     Action
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Drama


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt4566758|imdb|5.6|5.6|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 5.6/10 (107,162 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 78.4px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">5.6</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    A young Chinese maiden disguises herself as a male warrior in order to save her father.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Niki Caro  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Yifei Liu,
Donnie Yen,
Gong Li</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt4729430" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4729430">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4729430/?ref_=tt_sims_tti"><img height="190" width="128" alt="Klaus" title="Klaus" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMWYwOThjM2ItZGYxNy00NTQwLWFlZWEtM2MzM2Q5MmY3NDU5XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt4729430" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt4729430/?ref_=tt_sims_tt"><b>Klaus</b></a>
            <span class="nobr">(2019)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Klaus (2019)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt4729430|imdb|8.2|8.2|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.2/10 (104,487 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 114.8px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    A simple act of kindness always sparks another, even in a frozen, faraway place. When Smeerensburg's new postman, Jesper, befriends toymaker Klaus, their gifts melt an age-old feud and deliver a sleigh full of holiday traditions.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Sergio Pablos,
Carlos Martínez López  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Jason Schwartzman,
J.K. Simmons,
Rashida Jones</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt1049413" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt1049413">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt1049413/?ref_=tt_sims_tti"><img height="190" width="128" alt="Up" title="Up" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_UX128_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt1049413" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt1049413/?ref_=tt_sims_tt"><b>Up</b></a>
            <span class="nobr">(2009)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Up (2009)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt1049413|imdb|8.2|8.2|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.2/10 (935,088 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 114.8px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.2</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    78-year-old Carl Fredricksen travels to Paradise Falls in his house equipped with balloons, inadvertently taking a young stowaway.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Pete Docter,
Bob Peterson  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Edward Asner,
Jordan Nagai,
John Ratzenberger</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt7146812" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt7146812">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt7146812/?ref_=tt_sims_tti"><img height="190" width="128" alt="Onward" title="Onward" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMTZlYzk3NzQtMmViYS00YWZmLTk5ZTEtNWE0NGVjM2MzYWU1XkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt7146812" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt7146812/?ref_=tt_sims_tt"><b>Onward</b></a>
        <span>I</span>
            <span class="nobr">(2020)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Onward (2020)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt7146812|imdb|7.4|7.4|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 7.4/10 (99,887 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 103.6px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">7.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Two elven brothers embark on a quest to bring their father back for one day.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Dan Scanlon  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Tom Holland,
Chris Pratt,
Julia Louis-Dreyfus</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0198781" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0198781">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0198781/?ref_=tt_sims_tti"><img height="190" width="128" alt="Monsters, Inc." title="Monsters, Inc." src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMTY1NTI0ODUyOF5BMl5BanBnXkFtZTgwNTEyNjQ0MDE@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt0198781" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0198781/?ref_=tt_sims_tt"><b>Monsters, Inc.</b></a>
            <span class="nobr">(2001)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Monsters, Inc. (2001)" class="us_g titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0198781|imdb|8.1|8.1|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.1/10 (815,147 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 113.4px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.1</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, 2 monsters realize things may not be what they think.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Pete Docter,
David Silverman, <a href="fullcredits?ref_=tt_ov_dr#directors">and 1 more credit</a>&nbsp;»
  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Billy Crystal,
John Goodman,
Mary Gibbs</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0910970" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0910970">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0910970/?ref_=tt_sims_tti"><img height="190" width="128" alt="WALL·E" title="WALL·E" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt0910970" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0910970/?ref_=tt_sims_tt"><b>WALL·E</b></a>
            <span class="nobr">(2008)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for WALL·E (2008)" class="us_g titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Family


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0910970|imdb|8.4|8.4|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.4/10 (999,289 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 117.6px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Director:</b>
Andrew Stanton  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Ben Burtt,
Elissa Knight,
Jeff Garlin</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt4633694" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt4633694">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt4633694/?ref_=tt_sims_tti"><img height="190" width="128" alt="Spider-Man: Into the Spider-Verse" title="Spider-Man: Into the Spider-Verse" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_UY190_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt4633694" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt4633694/?ref_=tt_sims_tt"><b>Spider-Man: Into the Spider-Verse</b></a>
            <span class="nobr">(2018)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Spider-Man: Into the Spider-Verse (2018)" class="us_pg titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Action
     <span class="ghost">|</span> 
                     Adventure


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt4633694|imdb|8.4|8.4|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.4/10 (374,540 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 117.6px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.4</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Bob Persichetti,
Peter Ramsey, <a href="fullcredits?ref_=tt_ov_dr#directors">and 1 more credit</a>&nbsp;»
  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Shameik Moore,
Jake Johnson,
Hailee Steinfeld</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0266543" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0266543">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0266543/?ref_=tt_sims_tti"><img height="190" width="128" alt="Finding Nemo" title="Finding Nemo" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BZTAzNWZlNmUtZDEzYi00ZjA5LWIwYjEtZGM1NWE1MjE4YWRhXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX128_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt0266543" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0266543/?ref_=tt_sims_tt"><b>Finding Nemo</b></a>
            <span class="nobr">(2003)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for Finding Nemo (2003)" class="us_g titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Comedy


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0266543|imdb|8.1|8.1|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.1/10 (949,182 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 113.4px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.1</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Andrew Stanton,
Lee Unkrich  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Albert Brooks,
Ellen DeGeneres,
Alexander Gould</span></div>
           </div>

         </div>
       </div>

      </div>


      <div class="rec_overview" data-tconst="tt0110357" style="display: none;">

    
    
    <div class="rec_poster" data-info="" data-spec="p13nsims:tt2948372" data-tconst="tt0110357">
        <div class="rec_overlay">
            <div class="rec_filter"></div>
            <div class="glyph rec_watchlist_glyph"></div>
            <div class="glyph rec_blocked_glyph"></div>
            <div class="glyph rec_rating_glyph"></div>
            <div class="glyph rec_pending_glyph"></div>                        
        </div>            
<a href="/title/tt0110357/?ref_=tt_sims_tti"><img height="190" width="128" alt="The Lion King" title="The Lion King" src="https://m.media-amazon.com/images/S/sash/4FyxwxECzL-U1J8.png" class="loadlate rec_poster_img" loadlate="https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_UX128_CR0,0,128,190_AL_.jpg"> <br>
</a>    </div>


       <div class="rec_actions">

         <div class="rec_action_divider">
           <div class="wlb_classic_wrapper">
             <span class="wlb_wrapper">
               <a class="rec_wlb_watchlist_btn btn2_wrapper btn2_active wlb_lite" data-tconst="tt0110357" data-size="medium" data-caller-name="p13nsims-title" data-type="primary" data-tracking-tag="tt_sims_wl" data-initialized="1"><div class="btn2_alert" style="display:none"></div><a class="btn2 medium primary btn2_text_on" onclick="" title="Click to add to watchlist"><span class="btn2_glyph"></span><span class="btn2_text">Add to Watchlist</span></a></a>
             </span>
           </div>
         </div>


         <div class="rec_next_btn">
           <span class="btn2_wrapper">
             <a class="rec_next btn2 medium btn2_text_on" title="Show me the next title">
               <span class="btn2_text">Next »</span>
             </a>
           </span>
         </div>

             <input type="hidden" name="49e6c" value="58b0">
       </div>

       <div class="rec_details">
         <div class="rec-info">

           <div class="rec-jaw-upper">

     <div class="rec-title">
       <a href="/title/tt0110357/?ref_=tt_sims_tt"><b>The Lion King</b></a>
            <span class="nobr">(1994)</span>
   </div>



    <div class="rec-cert-genre rec-elipsis">





                    <span title="Ratings certificate for The Lion King (1994)" class="us_g titlePageSprite absmiddle"></span>

                     Animation
     <span class="ghost">|</span> 
                     Adventure
     <span class="ghost">|</span> 
                     Drama


    </div>

             <div class="rec-rating">





<div class="rating rating-list" data-starbar-class="rating-list" data-auth="" data-user="" id="tt0110357|imdb|8.5|8.5|p13nsims-title|tt2948372|title|main" data-ga-identifier="" title="Users rated this 8.5/10 (941,554 votes) - click stars to rate">
<span class="rating-bg">&nbsp;</span>
<span class="rating-imdb " style="width: 119px">&nbsp;</span>
<span class="rating-stars">
      <a rel="nofollow" title="Register or login to rate this title"><span>1</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>2</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>3</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>4</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>5</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>6</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>7</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>8</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>9</span></a>
      <a rel="nofollow" title="Register or login to rate this title"><span>10</span></a>
</span>
<span class="rating-rating "><span class="value">8.5</span><span class="grey">/</span><span class="grey">10</span></span>
<span class="rating-cancel "><a title="Delete" rel="nofollow"><span>X</span></a></span>
&nbsp;</div>

               <div class="rec-outline">
    <p>
    Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.    </p>
               </div>

             </div>

           </div>

           <div class="rec-jaw-lower">
             <div class="rec-jaw-teeth"></div>
 <div class="rec-director rec-ellipsis">
      <b>Directors:</b>
Roger Allers,
Rob Minkoff  </div>
<div class="rec-actor rec-ellipsis"> <span>
    <b>Stars:</b>
Matthew Broderick,
Jeremy Irons,
James Earl Jones</span></div>
           </div>

         </div>
       </div>

      </div>


   </div>


                    </div>
                </div>


  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleRecsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleRecsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleRecsWidget", {wb: 1});
    }
</script>






    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

        


    
    
    

        <!-- slot center-11 -->


    
    
    

	
	<!-- no content received for slot: maindetails_center_ad -->
	

        <!-- slot center-12 -->


    
    
    


        <!-- Storyline (includes keywords, taglines, genres, and certification summaries -->

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleStorylineWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleStorylineWidget_started');
    }
  </script>
    <div class="article" id="titleStoryLine">
    <span class="rightcornerlink">
            <a href="/register/login?why=edit&amp;ref_=tt_stry" rel="login">Edit</a>
    </span>
    
        <h2>Storyline</h2>
        
        <div class="inline canwrap">
            <p>
                <span>    Joe is a middle-school band teacher whose life hasn't quite gone the way he expected. His true passion is jazz -- and he's good. But when he travels to another realm to help someone find their passion, he soon discovers what it means to have soul.</span>
            </p>
        </div>
        
        <span class="see-more inline"> 
                <a href="/title/tt2948372/plotsummary?ref_=tt_stry_pl">Plot Summary</a>
    <span>|</span>
        <a href="/title/tt2948372/synopsis?ref_=tt_stry_pl">Plot Synopsis</a>
    </span>
        <hr>
        <div class="see-more inline canwrap">
            <h4 class="inline">Plot Keywords:</h4>
<a href="/search/keyword?keywords=jazz&amp;ref_=tt_stry_kw"> <span class="itemprop">jazz</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=purpose&amp;ref_=tt_stry_kw"> <span class="itemprop">purpose</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=cat&amp;ref_=tt_stry_kw"> <span class="itemprop">cat</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=school-teacher&amp;ref_=tt_stry_kw"> <span class="itemprop">school teacher</span></a>
                        <span>|</span>
<a href="/search/keyword?keywords=jazz-musician&amp;ref_=tt_stry_kw"> <span class="itemprop">jazz musician</span></a>
            <span>|</span>&nbsp;<nobr><a href="/title/tt2948372/keywords?ref_=tt_stry_kw">See All (64)</a>&nbsp;»</nobr>

        </div>      
        <hr>
        <div class="txt-block">
            <h4 class="inline">Taglines:</h4>
Everybody has a soul. Joe Gardner is about to find his.        </div>
        <hr>
        <div class="see-more inline canwrap">
            <h4 class="inline">Genres:</h4>
<a href="/search/title?genres=animation&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Animation</a>&nbsp;<span>|</span>
<a href="/search/title?genres=adventure&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Adventure</a>&nbsp;<span>|</span>
<a href="/search/title?genres=comedy&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Comedy</a>&nbsp;<span>|</span>
<a href="/search/title?genres=family&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Family</a>&nbsp;<span>|</span>
<a href="/search/title?genres=fantasy&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Fantasy</a>&nbsp;<span>|</span>
<a href="/search/title?genres=music&amp;explore=title_type,genres&amp;ref_=tt_ov_inf"> Music</a>
        </div>      
        
             <hr>
    
    <div class="txt-block">
                <h4>Motion Picture Rating
                    (<a href="/mpaa?ref_=tt_stry_pg">MPAA</a>)
                </h4>
            <span>Rated PG for thematic elements and some language</span>
    <span class="ghost">|</span>            <span class="see-more inline">
<a href="/title/tt2948372/parentalguide?ref_=tt_stry_pg#certification"> See all certifications</a>&nbsp;»
            </span>
    </div>
    <div class="txt-block">
        <h4 class="inline">Parents Guide:</h4>
        <span class="see-more inline">
<a href="/title/tt2948372/parentalguide?ref_=tt_stry_pg"> View content advisory</a>&nbsp;»
        </span>
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleStorylineWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleStorylineWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleStorylineWidget", {wb: 1});
    }
</script>

        <!-- Did You Know? -->

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDidYouKnowWidget_started');
    }
  </script>
    <div id="titleDidYouKnow" class="article">
    <span class="rightcornerlink">
            <a href="/register/login?why=edit&amp;ref_=tt_trv_trv" rel="login">Edit</a>
    </span>
        <h2>Did You Know?</h2>
    <div id="trivia" class="txt-block">
        <h4>Trivia</h4>
    <a href="/name/nm4456022?ref_=tt_trv_trv">Jon Batiste</a> composed jazz music for the film's New York City sequences, while <a href="/name/nm0722153?ref_=tt_trv_trv">Trent Reznor</a> and <a href="/name/nm1589604?ref_=tt_trv_trv">Atticus Ross</a> wrote an instrumental score for the scenes taking place in "The Great Before." Batiste said that he wanted to create jazz music that felt "authentic," but also "accessible to all ages." He also wanted the themes to tie into the "ethereal nature" of "The Great Before" while still being on Earth. Batiste also sometimes worked with Reznor and Ross to "blend the two worlds, musically."        <a href="trivia?ref_=tt_trv_trv" class="nobr">See more</a>  »
    </div>
                <hr>
     <div id="goofs" class="txt-block">
        <h4>Goofs</h4>
When Joe first lands in the Great Before, and the souls are playing with him, Jerry responds and apologizes for their behavior by saying, "Sorry, new souls. 37, that's enough!" But if 22 is one of the oldest souls in the Great Before, 37 would not be a new soul and would in fact be a very old soul.        <a href="trivia?tab=gf&amp;ref_=tt_trv_gf" class="nobr">See more</a>  »
    </div>   
                <hr>
    <div id="quotes" class="text-block">
        <h4>Quotes</h4>
[<span class="fine">first lines</span>]
<br><a href="/name/nm0004937/?ref_=tt_trv_qu"><span class="character">Joe</span></a>:
All right, let's try something else.
<br>[<span class="fine">tapping stick</span>]
<br><a href="/name/nm0004937/?ref_=tt_trv_qu"><span class="character">Joe</span></a>:
Uh, from the top. Ready. One, two, three.
<br>        <a href="trivia?tab=qt&amp;ref_=tt_trv_qu" class="nobr">See more</a> »
    </div>
                <hr>
     <div id="crazyCredits" class="txt-block">
        <h4>Crazy Credits</h4>
    The Walt Disney Pictures  orchestral version of "When You Wish Upon A Star" is played by the middle school jazz band, leading into the opening scene, and is somewhat off-key.        <a href="trivia?tab=cz&amp;ref_=tt_trv_cc" class="nobr">See more</a>  »
    </div>   
                <hr>
    <div id="connections" class="text-block">
        <h4>Connections</h4>
        Referenced in <a href="/title/tt12220734?ref_=tt_trv_cnn">AniMat's Crazy Cartoon Cast: Topsy Turvy Plans</a>&nbsp;(2020)


        <a href="trivia?tab=mc&amp;ref_=tt_trv_cnn" class="nobr">See more</a> »
    </div>
                <hr>
    <div id="soundtracks" class="text-block">
        <h4>Soundtracks</h4>
Things Ain't What They Used to Be <br>
(instrumental) <br>
Written by <a href="/name/nm0254160/">Mercer Ellington</a> <br>        <a href="soundtrack?ref_=tt_trv_snd" class="nobr">See more</a> »
    </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDidYouKnowWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleDidYouKnowWidget", {wb: 1});
    }
</script>

        <!-- slot center-13 -->


    
    
    

        <!-- User Reviews (one-item summary) -->


<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleUserReviewsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_started');
    }
  </script>
    <div class="article" id="titleUserReviewsTeaser">
        <h2>User Reviews</h2>
        <div class="user-comments">
                    <div class="tinystarbar" title="8/10">
                        <div style="width: 80px;">&nbsp;</div>
                    </div>
                <span>
                    <strong>Loved it almost to tears (and I'm a big man with a beard)</strong>
                    <div class="comment-meta">
                        26 December 2020 | by <a href="/user/ur19510928/?ref_=tt_urv"><span>Bert08</span></a>
                        – <a href="/user/ur19510928/comments?ref_=tt_urv">See all my reviews</a>
                    </div>
                    <div>
                        <p>Before explaining why I liked this movie, I'd like to point out that the main idea of the movie is *NOT* that you need find your purpose to have a happy life. It's the exact opposite! I'm not saying this just to be a professor, but because it's really important and that's why I loved the film so much. You don't need to be fixated about something to find a meaning in your life. You need to savour it and learn to enjoy the little moments instead of waiting for something big to happen to reach happiness. It's so profound and refreshing. A movie just about a guy waiting for his big moment and feeling fulfilled after having reached it would have been dull, boring, trite and most of all wrong, like pretty much all "self-help" advices.
Instead the opposite idea is presented and if you just pay attention to the dialogues -and the story, really- you'll understand what I mean and most importantly what you might apply to make your everyday life better.
But back to the movie I've got to say I almost cried as the end was approaching as much as I was going to turn off the tv when the movie started. The whole initial setting reminded me too much of Inside Out, a film I quite disliked, so I was worried it was a copy of it (it kind of is in the beginnin). But luckily the second half steered away from it and developed in one of the most moving film I've seen in a long time. Undoubtedly one of Pixar's best.</p>
                    </div>
                </span>
                <hr>


                <div class="yn" id="ynd_rw6401046">
                400 of 470 people found this review helpful.&nbsp;
                Was this review helpful to you?

                    <button class="btn small" value="Yes" name="ynb_rw6401046_yes" onclick="CS.TMD.user_review_vote('rw6401046', 'tt2948372', 'yes', 'true');">Yes</button>
                    <button class="btn small" value="No" name="ynb_rw6401046_no" onclick="CS.TMD.user_review_vote('rw6401046', 'tt2948372', 'no', 'true');">No</button>
                        | <a href="/registration/signin?u=/title/tt2948372/&amp;ref_=tt_urv" onclick="imdb.contribution.clickHandler(event)">Report this</a>
                </div>

                <a href="/registration/signin?u=/title/tt2948372/&amp;ref_=tt_urv" onclick="imdb.contribution.clickHandler(event)">Review this title</a>

            <span>|</span>
            <a href="/title/tt2948372/reviews?ref_=tt_urv">See all 1,359 user reviews</a>&nbsp;»
        </div>
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_finished');
    }
  </script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleUserReviewsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleUserReviewsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleUserReviewsWidget", {wb: 1});
    }
</script>

        <!-- FAQ -->
<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleFAQWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleFAQWidget_started');
    }
  </script>
    
    <div class="article" id="titleFAQ">
        <h2>Frequently Asked Questions</h2>
        
            <div class="faq">
                    <div class="odd">
                    <b>Q:</b>
<a href="/title/tt2948372/faq?ref_=tt_faq_1#fq0121055"> Is Joe really the first person to ever reject being dead?</a>
                    </div>
                    <div class="even">
                    <b>Q:</b>
<a href="/title/tt2948372/faq?ref_=tt_faq_2#fq0118255"> When will they release this film on DVD?</a>
                    </div>
                    <div class="odd">
                    <b>Q:</b>
<a href="/title/tt2948372/faq?ref_=tt_faq_3#fq0121540"> What do the lost souls mean by "Make a trade", which they spookily repeat over and over again?</a>
                    </div>
            </div>
        
            <span class="see-more inline">        
                <a href="/title/tt2948372/faq?ref_=tt_faq_sm" class="nobr">See more</a>
            </span> »
    </div>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleFAQWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleFAQWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleFAQWidget", {wb: 1});
    }
</script>

        <!-- Details -->

<script>
    if (typeof uet == 'function') {
      uet("bb", "TitleDetailsWidget", {wb: 1});
    }
</script>
  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDetailsWidget_started');
    }
  </script>

    <div class="article" id="titleDetails">
    <span class="rightcornerlink">
            <a href="/register/login?why=edit&amp;ref_=tt_dt_dt" rel="login">Edit</a>
    </span>
        <h2>Details</h2>
      <div class="txt-block">
      <h4 class="inline">Official Sites:</h4>
    <a href="/offsite/?page-action=offsite-disneyplus&amp;token=BCYisZ6OPwMeTsJ9foWfKMfPXfRv_7IdcbjHIt_TGsCTWK3cncONnFM7Zg4QNGc9yE_Fi5E4Kpfa%0D%0A-f_9qdiU138_-q-i7c4HcnznpgPvQYPFjL5Ep5lUaxhA8mTxS5MyLSUizH5DcM03T7J8jWqsJdes%0D%0AKT94uRyGHwsByjovNc5pHrkYY3UDrcGFl6oPjoFogXB4dkwRxi6XDTevsxajqCZa7jyYZF2HWZt7%0D%0AQMykIPncHAPl27BLkH-RrJW-N2MS3VKt%0D%0A&amp;ref_=tt_pdt_ofs_offsite_0" rel="nofollow">Disney+</a>
          <span class="ghost">|</span>
        
    <a href="/offsite/?page-action=offsite-disney&amp;token=BCYtgEGqY8nwEftJkIU9H9PJMXM6DTYxPXYJeigfjnlVF2P2iOpRTstEJOpb7lD2pIwEBNgw4bpn%0D%0AmL07VrPnN-mKHH8kQ5SLyQiqeetT9Z1-UrAN7nxwox8IqEA1ZbBuFJFOUeuFsicXlcJSjC7g5mUO%0D%0ATvLLt8Z6rLDfCwBl-nEeIAYgbTu5EUEhun_B--2RqDfsgmNrhopAXN8X2B_oXY866WNFB4LZpLdM%0D%0Aqw4F0Ylw5Bs%0D%0A&amp;ref_=tt_pdt_ofs_offsite_1" rel="nofollow">Official site</a>
          <span class="ghost">|</span>
               <span class="see-more inline">
          <a href="externalsites?ref_=tt_dt_dt#official">See more</a>&nbsp;»
      </span>
      </div>

    <div class="txt-block">
    <h4 class="inline">Country:</h4>
        <a href="/search/title?country_of_origin=us&amp;ref_=tt_dt_dt">USA</a>
    </div>

    <div class="txt-block">
    <h4 class="inline">Language:</h4>
        <a href="/search/title?title_type=feature&amp;primary_language=en&amp;sort=moviemeter,asc&amp;ref_=tt_dt_dt">English</a>
    </div>


    <div class="txt-block">
    <h4 class="inline">Release Date:</h4> 25 December 2020 (USA)
    <span class="see-more inline">
      <a href="releaseinfo?ref_=tt_dt_dt">See more</a>&nbsp;»
    </span>
    </div>

      <div class="txt-block">
      <h4 class="inline">Also Known As:</h4> Soul
      <span class="see-more inline">
        <a href="releaseinfo?ref_=tt_dt_dt#akas">See more</a>&nbsp;»
      </span>
      </div>

    <div class="txt-block">
    <h4 class="inline">Filming Locations:</h4>
    <a href="/search/title?locations=New%20York%20City,%20New%20York,%20USA&amp;ref_=tt_dt_dt">New York City, New York, USA</a>
      <span class="see-more inline">
        <a href="locations?ref_=tt_dt_dt">See more</a>&nbsp;»
      </span>
    </div>

    <hr>
    <span class="rightcornerlink">
            <a href="/register/login?why=edit&amp;ref_=tt_dt_bo" rel="login">Edit</a>
    </span>
    <h3 class="subheading">Box Office</h3>




        <div class="txt-block">
<h4 class="inline">Cumulative Worldwide Gross:</h4> $71,200,000        </div>

    <span class="see-more inline">
        <a href="https://pro.imdb.com/title/tt2948372?rf=cons_tt_bo_tt&amp;ref_=cons_tt_bo_tt">See more on IMDbPro</a>&nbsp;»
    </span>
  <hr>
  <h3 class="subheading">Company Credits</h3>
    <div class="txt-block">
    <h4 class="inline">Production Co:</h4>
<a href="/company/co0008970?ref_=cons_tt_dt_co_1"> Walt Disney Pictures</a>,<a href="/company/co0017902?ref_=cons_tt_dt_co_2"> Pixar Animation Studios</a>      <span class="see-more inline">
        <a href="companycredits?ref_=tt_dt_co">See more</a>&nbsp;»
      </span>
    </div>
  <div class="txt-block">
  Show more on
  <a href="https://pro.imdb.com/title/tt2948372/companycredits?rf=cons_tt_cocred_tt&amp;ref_=cons_tt_cocred_tt">IMDbPro</a>&nbsp;»
  </div>


  <hr>
  <h3 class="subheading">Technical Specs</h3>

    <div class="txt-block">
      <h4 class="inline">Runtime:</h4>
        <time datetime="PT100M">100 min</time>
    </div>

    <div class="txt-block">
    <h4 class="inline">Sound Mix:</h4>
        <a href="/search/title?sound_mixes=dolby_atmos&amp;ref_=tt_dt_spec">Dolby Atmos</a>
    </div>

    <div class="txt-block">
    <h4 class="inline">Color:</h4>
        <a href="/search/title?colors=color&amp;ref_=tt_dt_spec">Color</a>
    </div>

    <div class="txt-block">
    <h4 class="inline">Aspect Ratio:</h4> 2.39 : 1
    </div>

  See <a href="technical?ref_=tt_dt_spec">full technical specs</a>&nbsp;»
    </div>

  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleDetailsWidget_finished');
    }
  </script>
<script>
    if (typeof uet == 'function') {
      uet("be", "TitleDetailsWidget", {wb: 1});
    }
</script>
<script>
    if (typeof uex == 'function') {
      uex("ld", "TitleDetailsWidget", {wb: 1});
    }
</script>

        <!-- slot center-14 -->


    
    
    

        <!-- slot center-15 -->


    
    
    


            <!-- slot center-16 -->


    
    
    


            <!-- slot center-17 -->


    
    
    

            <!-- slot center-18 -->


    
    
    

            <!-- slot center-19 -->


    
    
    

            <!-- Contribute to This Page -->

  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleContributeWidget_started');
    }
  </script>
    <div class="article contribute">
        <div class="rightcornerlink">
<a href="https://help.imdb.com/article/contribution/contribution-information/adding-data/G6BXD2JFDCCETUF4?ref_=cons_tt_cn_gs_hlp">Getting Started</a>
            <span>|</span>
<a href="/czone/?ref_=tt_cn_cz">Contributor Zone</a>&nbsp;»</div>
        <h2>Contribute to This Page</h2>

                <div class="button-box">
                    <form method="get" action="https://contribute.imdb.com/updates">
                        <input type="hidden" name="ref_" value="tt_cn_edt">
                        <input type="hidden" name="edit" value="legacy/title/tt2948372/">
                            <button class="btn primary large" rel="login" type="submit">Edit page</button>
                    </form>
                </div>





    </div>

  <script>
    if ('csm' in window) {
      csm.measure('csm_TitleContributeWidget_finished');
    }
  </script>


    
    
    

            <!-- slot center-20 -->


    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    </div>"""
    
page_soup = soup(html_doc, 'html.parser')
main = soup(html2, 'html.parser')
# print(page_soup.prettify())
# print(main.prettify())


details = page_soup.find('div', id='title-overview-widget')
# print(details.prettify())

title = details.h1.text
# print(title.split('\xa0'))
title = ' '.join(title.split('\xa0')[:-1])
# print(title)

subtext = details.find('div', class_='subtext')
release_date = subtext.find(title='See more release dates').text
split = release_date.split(' ')
if len(split) > 3:
    release_date = ' '.join(split[:3])
# print(release_date)
    
infos = details.find_all('div', class_='credit_summary_item')
for info in infos:
    if info.h4.text == 'Writers:':
        continue
    else:
        people = info.find_all('a')
        if 'See full' in people[-1].text:
            people = people[:-1]
    # print([person.text for person in people])

storyline = main.find_all('div', class_='see-more inline canwrap')
for thing in storyline:
    if thing.h4.text == 'Genres:':
        genres = thing.find_all('a')
        # print([genre.text for genre in genres])


cast_body = """<tbody><tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/kanye-west?filter-options=movies">
                                                    Kanye West
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        7
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">52</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">5
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/christina-aguilera?filter-options=movies">
                                                    Christina Aguilera
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        7
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">48</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">9
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/jay-z?filter-options=movies">
                                                    Jay-Z
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        11
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">51</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">6
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/nas?filter-options=movies">
                                                    Nas
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        4
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">63</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">6
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/katy-perry?filter-options=movies">
                                                    Katy Perry
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        6
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">53</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">5
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/lady-gaga?filter-options=movies">
                                                    Lady Gaga
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        10
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">62</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">4
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/britney-spears?filter-options=movies">
                                                    Britney Spears
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        1
                        Movie                    </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_unfavorable">27</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">31
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/rihanna?filter-options=movies">
                                                    Rihanna
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        9
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">57</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">0
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/kid-cudi?filter-options=movies">
                                                    Kid Cudi
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        4
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">40</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">18
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/phoebe-waller-bridge?filter-options=movies">
                                                    Phoebe Waller-Bridge
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        3
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">62</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">4
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/demi-lovato?filter-options=movies">
                                                    Demi Lovato
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        6
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">44</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">14
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/madonna?filter-options=movies">
                                                    Madonna
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        15
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">40</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">17
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/janelle-monae?filter-options=movies">
                                                    Janelle Monáe
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        9
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">57</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">0
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/selena-gomez?filter-options=movies">
                                                    Selena Gomez
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        19
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">48</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">10
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/eminem?filter-options=movies">
                                                    Eminem
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        4
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">71</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">13
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/ben-howard?filter-options=movies">
                                                    Ben Howard
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        3
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">52</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">6
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/teyana-taylor?filter-options=movies">
                                                    Teyana Taylor
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        1
                        Movie                    </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">45</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">13
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/miley-cyrus?filter-options=movies">
                                                    Miley Cyrus
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        8
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">53</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">5
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/brad-pitt?filter-options=movies">
                                                    Brad Pitt
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        75
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">64</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">7
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/paul-schrader?filter-options=movies">
                                                    Paul Schrader
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        28
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">64</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">6
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/mariah-carey?filter-options=movies">
                                                    Mariah Carey
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        8
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">52</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">6
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/bjork?filter-options=movies">
                                                    Björk
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        8
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">64</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">6
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/paul-bettany?filter-options=movies">
                                                    Paul Bettany
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        34
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">57</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">1
                                point                                lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/eva-lazzaro?filter-options=movies">
                                                    Eva Lazzaro
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        2
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">71</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">13
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/josh-brolin?filter-options=movies">
                                                    Josh Brolin
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        44
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">58</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">1
                                point                                higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/barry-josephson?filter-options=movies">
                                                    Barry Josephson
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        13
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">45</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">12
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/kent-kubena?filter-options=movies">
                                                    Kent Kubena
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        6
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">42</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">15
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/luis-chavez?filter-options=movies">
                                                    Luis Chávez
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        3
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">41</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">16
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/volker-engel?filter-options=movies">
                                                    Volker Engel
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        4
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_mixed">46</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_terrible">
                            <span class="avg_score">12
                                 points                                 lower                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
                                
                            
            
            <tr class="details_section">
                <td class="title_wrapper">
                    <div class="title">
                        <a href="/person/brie-larson?filter-options=movies">
                                                    Brie Larson
                                                </a>
                    </div>
                                        <div class="counts">
                                                                        25
                         Movies                     </div>
                </td>
                <td class="details_wrapper">
                                            <span class="avg_score">Average score: <span class="textscore_favorable">62</span></span>
                    
                    <div>
                        On average, this person grades
                        <span class="comparative textscore_outstanding">
                            <span class="avg_score">4
                                 points                                 higher                            </span>
                        </span>
                        than other people.
                    </div>
                </td>
            </tr>
            </tbody>"""

main = """<div id="main" class="col main_col">
                <div class="person_header">
                    
                        
            <div class="sharing ">
    
    <a class="sharing-facebook" title="Share on Facebook" rel="nofollow noopener popup:external" data-mc-social-url="https://www.metacritic.com/person/eminem?ftag=fbsoshares" href="javascript:void(0);"><span class="fa fa-fw fa-facebook"></span></a><a class="sharing-twitter" title="Share on Twitter" rel="nofollow noopener popup:external" href="https://twitter.com/intent/tweet?via=metacritic&amp;text=Eminem%20Movies%20Profile&amp;url=http%3A%2F%2Fmtcr.tc%2F3046bb4" target="_blank"><span class="fa fa-fw fa-twitter"></span></a><a class="sharing-reddit" title="Share on Reddit" rel="nofollow noopener popup:external" data-mc-social-track-id="6" target="_blank" href="https://www.reddit.com/submit?url=https%3A%2F%2Fwww.metacritic.com%2Fperson%2Feminem%3Fftag%3Dredsoshares&amp;title=Eminem%20Movies%20Profile"><span class="fa fa-fw fa-reddit-alien"></span></a><a class="sharing-pinterest" title="Share on Pinterest" rel="nofollow noopener popup:external" data-mc-social-track-id="5" target="_blank" href="//pinterest.com/pin/create/link/?url=https%3A%2F%2Fwww.metacritic.com%2Fperson%2Feminem%3Fftag%3Dpinsoshares&amp;description=Eminem%20Movies%20Profile&amp;media=https://static.metacritic.com/images/icons/mc_fb_og.png"><span class="fa fa-fw fa-pinterest"></span></a></div>


            <h1 class="person_title">
        Eminem
    </h1>
				<p></p>
</div>


 <div class="module credits_module person_credits_module">
    <div class="head head_type_1"><div class="head_wrap"><h2 class="module_title">Eminem's Scores</h2>                            <ul class="tabs tabs_type_1">            <li class="tab tab_type_1 tab_movies first">
                                    <span class="active"><span>Movies</span></span>
                            </li>
                                                        <li class="tab tab_type_1 tab_tv">
                                                        <a href="/person/eminem?filter-options=tv&amp;sort_options=date&amp;num_items=30"><span>TV</span></a>
                            </li>
                                                        <li class="tab tab_type_1 tab_music">
                                                        <a href="/person/eminem?filter-options=music&amp;sort_options=date&amp;num_items=30"><span>Music</span></a>
                            </li>
                                                        <li class="tab tab_type_1 tab_games last">
                                                        <a href="/person/eminem?filter-options=games&amp;sort_options=date&amp;num_items=30"><span>Games</span></a>
                            </li>
            </ul>            
    
    
    
    
</div></div>

		<div class="score_details personscore_details">
    <div class="score_details_wrap">
        <div class="profile_score_summary personscore_summary">
            <table class="profile_score_summary personscore_summary" summary=" Review Score Summaries">
                <tbody><tr class="review_average">
                                            <th scope="row" class="summary_label">Average career score:</th>
                        <td class="summary_score" colspan="2">
                                                                    <span class="data textscore textscore_favorable">71</span>

                                                    </td>
                                    </tr>
                                    <tr class="highest_review">
                        <th scope="row" class="summary_label">Highest Metascore:</th>
                        <td class="summary_score">
                            

        
<span class="metascore_w small movie positive indiv">77</span>

                        </td>
                        <td class="summary_data">
                            <span class="product_title">
                                <a href="/movie/8-mile">8 Mile</a>
                            </span>
                        </td>
                    </tr>
                                                    <tr class="lowest_review last">
                        <th scope="row" class="summary_label">Lowest Metascore:</th>
                        <td class="summary_score">
                            

        
<span class="metascore_w small movie positive indiv">63</span>

                        </td>
                        <td class="summary_data">
                            <span class="product_title">
                                <a href="/movie/freestyle-the-art-of-rhyme">Freestyle: The Art of Rhyme</a>
                            </span>
                        </td>
                    </tr>
                            </tbody></table>
        </div>
        <div class="score_distribution">
    <div class="distribution_wrap">
        <div class="distribution_title">Score distribution:</div>
        <ol class="score_counts hover_none">
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Positive:</span>
                    <span class="data">
                        <a href="/person/eminem?filter-options=movies&amp;sort_options=date&amp;dist=positive&amp;num_items=30">                            <span class="total" style="width:100%;">
                                <span class="count">4</span>
                                <span class="distribution positive"> out of 4</span>
                            </span>
                        </a>                    </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Mixed:</span>
                    <span class="data">
                                                    <span class="total zero_total" style="width:0%;">
                                <span class="count">0</span>
                                <span class="distribution mixed"> out of 4</span>
                            </span>
                                            </span>
                </div>
            </li>
                        <li class="score_count">
                <div class="count_wrap">
                    <span class="label">Negative:</span>
                    <span class="data">
                                                    <span class="total zero_total" style="width:0%;">
                                <span class="count">0</span>
                                <span class="distribution negative"> out of 4</span>
                            </span>
                                            </span>
                </div>
            </li>
                    </ol>
		            <div class="reviews_total">
                <span class="count">
                                    
                                					<a href="/person/eminem">4</a> 
				                </span>
                                    <span>
                                            movie
                     reviews</span>
                            </div>
		    </div>
</div>

    </div>
</div>

    <div class="body">
                            <div class="tabs ">
        <div class="tab_wrap">
                            <ul class="tabs tabs_type_1">            <li class="tab tab_type_1 tab_date first">
                                    <span class="active"><span>By date</span></span>
                            </li>
                                                        <li class="tab tab_type_1 tab_metascore">
                                                        <a href="/person/eminem?filter-options=movies&amp;sort_options=metascore&amp;num_items=30"><span>By Metascore</span></a>
                            </li>
                                                        <li class="tab tab_type_1 tab_user_score last">
                                                        <a href="/person/eminem?filter-options=movies&amp;sort_options=user_score&amp;num_items=30"><span>By user score</span></a>
                            </li>
            </ul>            
            <div class="tab_options_wrap">
                            <div class="page_nav_options">
    <div class="options_wrap">
        <div class="label">view</div>
        <div class="options">
            <ul class="options">
                <li class="option">
                                                                <span>30</span>
                                    </li>
                <li class="option">
                                                                <a href="/person/eminem?filter-options=movies&amp;sort_options=date&amp;num_items=100"><span>100</span></a>
                                    </li>
            </ul>
        </div>
        <div class="desc">per page</div>
    </div>
</div>

                                </div>
    
    
            </div>
    </div>
    
    

        		            <table class="credits person_credits">
                <colgroup>
                    <col class="credit_title">
                    <col class="credit_year">
                                            <col class="credit_role">
                                        <col class="credit_userscore">
                </colgroup>
                <thead>
                    <tr>
                        <th class="credit_title">Title:</th>
                        <th class="credit_year">Year:</th>
                                                    <th class="credit_role">Credit:</th>
                                                <th class="credit_userscore">User score:</th>
                    </tr>
                </thead>
                <tbody>
                                    <tr>
                        <td class="title brief_metascore">
                             

        
<span class="metascore_w small movie positive">75</span>

                            <a href="/movie/bodied">Bodied</a>
                        </td>
                        <td class="year">
                                                            Nov 2, 2018
                                                    </td>
                                                    <td class="role">Producer / Producer</td>
                                                <td class="score">
                            


        <span class="data textscore textscore_mixed">5.6</span>

                        </td>
                    </tr>
                                    <tr class="alt">
                        <td class="title brief_metascore">
                             

        
<span class="metascore_w small movie positive">69</span>

                            <a href="/movie/how-to-make-money-selling-drugs">How to Make Money Selling Drugs</a>
                        </td>
                        <td class="year">
                                                            Jun 26, 2013
                                                    </td>
                                                    <td class="role">Himself / Himself</td>
                                                <td class="score">
                            


        <span class="data textscore textscore_outstanding">8.8</span>

                        </td>
                    </tr>
                                    <tr>
                        <td class="title brief_metascore">
                             

        
<span class="metascore_w small movie positive">63</span>

                            <a href="/movie/freestyle-the-art-of-rhyme">Freestyle: The Art of Rhyme</a>
                        </td>
                        <td class="year">
                                                            Jul 16, 2004
                                                    </td>
                                                    <td class="role">Himself</td>
                                                <td class="score">
                            


        <span class="data textscore textscore_outstanding">8.0</span>

                        </td>
                    </tr>
                                    <tr class="alt">
                        <td class="title brief_metascore">
                             

        
<span class="metascore_w small movie positive">77</span>

                            <a href="/movie/8-mile">8 Mile</a>
                        </td>
                        <td class="year">
                                                            Nov 8, 2002
                                                    </td>
                                                    <td class="role">Jimmy 'B-Rabbit' Smith</td>
                                                <td class="score">
                            


        <span class="data textscore textscore_outstanding">8.7</span>

                        </td>
                    </tr>
                                </tbody>
            </table>
                    
    </div>
</div>


                                                            <div class="mc_obbtm">
                        
        <div id="taboola-below-content-thumbnails"></div>
        
        <script type="text/javascript">
            var placement = 'desktop about Below Content Thumbnails';
            window._taboola = window._taboola || [];
                _taboola.push({
                mode: 'alternating-thumbnails-a',
                container: 'taboola-below-content-thumbnails',
                placement: placement,
                target_type: 'mix'
            });
        </script>
        



                        </div>
                                                </div>"""
                                                

cast_soup = soup(cast_body, 'html.parser')
main = soup(main, 'html.parser')
# print(cast_soup.prettify())

people = cast_soup.find_all('div', class_='title')
# print(people)
# for person in people:
    # print(person.select('a')[0]['href'])
    
# print(main.prettify())

# get name
title = main.find('h1', class_='person_title').text
# print(str(title).strip())

movies = main.find('table', class_='credits person_credits')
movie_list = movies.find('tbody').find_all('tr')
for movie in movie_list:
    name = movie.find('a').text.strip()
    print(name)
    year = movie.find('td', class_='year').text.strip().split(' ')[-1]
    print(year)
    role = movie.find('td', class_='role').text.strip()
    print(role)
    print('==================================================')