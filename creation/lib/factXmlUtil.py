import os

def get_submit_dir(conf_dom):
    return os.path.join(conf_dom.getElementsByTagName(u'submit')[0].getAttribute(u'base_dir'),
        u"glidein_%s" % conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name'))

def get_stage_dir(conf_dom):
    return os.path.join(conf_dom.getElementsByTagName(u'stage')[0].getAttribute(u'base_dir'),
        u"glidein_%s" % conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name'))

def get_monitor_dir(conf_dom):
    return os.path.join(conf_dom.getElementsByTagName(u'monitor')[0].getAttribute(u'base_dir'),
        u"glidein_%s" % conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name'))

def get_log_dir(conf_dom):
    return os.path.join(conf_dom.getElementsByTagName(u'submit')[0].getAttribute(u'base_log_dir'),
        u"glidein_%s" % conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name'))

def get_client_log_dirs(conf_dom):
    cl_dict = {}
    client_dir = conf_dom.getElementsByTagName(u'submit')[0].getAttribute(u'base_client_log_dir')
    glidein_name = conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name')
    for sc in conf_dom.getElementsByTagName(u'security_class'):
        cl_dict[sc.getAttribute(u'username')] = os.path.join(client_dir,
            u"user_%s" % sc.getAttribute(u'username'), u"glidein_%s" % glidein_name)

    return cl_dict

def get_client_proxy_dirs(conf_dom):
    cp_dict = {}
    client_dir = conf_dom.getElementsByTagName(u'submit')[0].getAttribute(u'base_client_proxies_dir')
    glidein_name = conf_dom.getElementsByTagName(u'glidein')[0].getAttribute(u'glidein_name')
    for sc in conf_dom.getElementsByTagName(u'security_class'):
        cp_dict[sc.getAttribute(u'username')] = os.path.join(client_dir,
            u"user_%s" % sc.getAttribute(u'username'), u"glidein_%s" % glidein_name)

    return cp_dict

def get_condor_tarballs(conf_dom):
    tarballs = []
    for tb in conf_dom.getElementsByTagName(u'condor_tarball'):
        tb_dict = {}
        tb_dict[u'arch'] = tb.getAttribute(u'arch')
        tb_dict[u'os'] = tb.getAttribute(u'os')
        tb_dict[u'tar_file'] = tb.getAttribute(u'tar_file')
        tb_dict[u'version'] = tb.getAttribute(u'version')
        tarballs.append(tb_dict)

    return tarballs

def get_files(conf_dom):
    files = []
    files_el = conf_dom.getElementsByTagName(u'files')[-1]
    for f in files_el.getElementsByTagName(u'file'):
        file_dict = {}
        if f.hasAttribute(u'absfname'):
            file_dict[u'absfname'] = f.getAttribute(u'absfname')
        else:
            file_dict[u'absfname'] = None
        if f.hasAttribute(u'after_entry'):
            file_dict[u'after_entry'] = f.getAttribute(u'after_entry')
        if f.hasAttribute(u'const'):
            file_dict[u'const'] = f.getAttribute(u'const')
        else:
            file_dict[u'const'] = u'False'
        if f.hasAttribute(u'executable'):
            file_dict[u'executable'] = f.getAttribute(u'executable')
        else:
            file_dict[u'executable'] = u'False'
        if f.hasAttribute(u'relfname'):
            file_dict[u'relfname'] = f.getAttribute(u'relfname')
        else:
            file_dict[u'relfname'] = None
        if f.hasAttribute(u'untar'):
            file_dict[u'untar'] = f.getAttribute(u'untar')
        else:
            file_dict[u'untar'] = u'False'
        if f.hasAttribute(u'wrapper'):
            file_dict[u'wrapper'] = f.getAttribute(u'wrapper')
        else:
            file_dict[u'wrapper'] = u'False'
        uopts = f.getElementsByTagName(u'untar_options')
        if len(uopts) > 0:
            uopt_el = f.getElementsByTagName(u'untar_options')[0]
            uopt_dict = {}
            if uopt_el.hasAttribute(u'absdir_outattr'):
                uopt_dict[u'absdir_outattr'] = uopt_el.getAttribute(u'absdir_outattr')
            else:
                uopt_dict[u'absdir_outattr'] = None
            if uopt_el.hasAttribute(u'dir'):
                uopt_dict[u'dir'] = uopt_el.getAttribute(u'dir')
            else:
                uopt_dict[u'dir'] = None
            uopt_dict[u'cond_attr'] = uopt_el.getAttribute(u'cond_attr')
            file_dict[u'untar_options'] = uopt_dict
            
        files.append(file_dict)

    return files