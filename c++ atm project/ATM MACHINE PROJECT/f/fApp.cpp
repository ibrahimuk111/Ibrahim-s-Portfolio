/***************************************************************
 * Name:      fApp.cpp
 * Purpose:   Code for Application Class
 * Author:    ff ()
 * Created:   2025-03-04
 * Copyright: ff ()
 * License:
 **************************************************************/

#ifdef WX_PRECOMP
#include "wx_pch.h"
#endif

#ifdef __BORLANDC__
#pragma hdrstop
#endif //__BORLANDC__

#include "fApp.h"
#include "fMain.h"

IMPLEMENT_APP(fApp);

bool fApp::OnInit()
{
    
    fDialog* dlg = new fDialog(0L, _("wxWidgets Application Template"));
    dlg->SetIcon(wxICON(aaaa)); // To Set App Icon
    dlg->Show();
    return true;
}
